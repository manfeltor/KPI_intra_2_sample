import requests
import time
import json
import re
from django.core.management.base import BaseCommand
from django.db import transaction
from entregasapp.models import bdoms, TrackingEventCA, ProcessingState
from entregasapp.selializers import TrackingEventCASerializer

from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
CAKEY = config('CAKEY')
CAAGREEMENT = config('CAAGREEMENT')
CATRKURL = config('CATRKURL')
CATOKEN = config('CATOKEN')

class Command(BaseCommand):
    help = 'Populate TrackingEventCA model with data from an external API'

    API_URL = CATRKURL
    HEADERS = {
        "authorization": CAKEY,
        "agreement": CAAGREEMENT,
    }
    VALID_TRACKING_REGEX = re.compile(r'^19.{16}$')  # Adjust the length as needed

    def handle(self, *args, **kwargs):
        last_processed_tracking = self.get_last_processed_tracking()
        
        # Fetch tracking numbers from bdoms and filter with regex
        tracking_numbers = list(
            bdoms.objects.filter(trackingTransporte__isnull=False)
            .order_by('fechaCreacion')
            .values_list('trackingTransporte', flat=True)
            .distinct()
        )

        # Find the index to resume from
        if last_processed_tracking:
            start_index = tracking_numbers.index(last_processed_tracking) + 1
        else:
            start_index = 0

        # Filter tracking numbers with regex
        valid_tracking_numbers = [tn for tn in tracking_numbers[start_index:] if self.VALID_TRACKING_REGEX.match(tn)]

        if not valid_tracking_numbers:
            self.stdout.write(self.style.WARNING("No valid tracking numbers found in bdoms."))
            return

        # Process batches
        batch_size = 20
        batch_delay = 1
        error_delay = 4
        retries = 3
        successful_requests = 0
        cached_data = []
        total_batches = (len(valid_tracking_numbers) + batch_size - 1) // batch_size
        atomizer_trigger = 10

        for i in range(total_batches):
            batch = valid_tracking_numbers[i * batch_size:(i + 1) * batch_size]
            if not batch:
                break

            for attempt in range(retries):
                try:
                    parameters = {
                        "extClient": "",
                        "trackingNumbers": batch
                    }
                    print(f"Requesting batch: {parameters}")  # Debugging line
                    response = requests.get(self.API_URL, headers=self.HEADERS, params=parameters)
                    response.raise_for_status()
                    data = response.json()
                    
                    # Cache the response data
                    for item in data:
                        tracking_event_data = {
                            'tracking_number': item.get('trackingNumber'),
                            'raw_data': json.dumps(item)  # Convert to JSON string
                        }
                        cached_data.append(tracking_event_data)
                    
                    successful_requests += 1
                    print(f"batch {successful_requests} ok")
                    
                    if successful_requests % atomizer_trigger == 0:
                        self.stdout.write(self.style.SUCCESS("Processed 500 successful requests."))
                        self.save_cached_data(cached_data)
                        cached_data = []  # Clear cache after saving

                    # Update the last processed tracking number
                    self.update_last_processed_tracking(batch[-1])

                    time.sleep(batch_delay)
                    break  # Exit retry loop on success
                except requests.RequestException as e:
                    self.stdout.write(self.style.ERROR(f"Request failed for batch {batch}: {e}"))
                    time.sleep(error_delay)
                    if attempt == retries - 1:
                        self.stdout.write(self.style.ERROR(f"Failed to process batch {batch} after {retries} attempts."))
                        return

        # Save any remaining cached data
        if cached_data:
            self.save_cached_data(cached_data)

    @transaction.atomic
    def save_cached_data(self, cached_data):
        for item in cached_data:
            serializer = TrackingEventCASerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                self.stdout.write(self.style.ERROR(f"Invalid data for {item['tracking_number']}: {serializer.errors}"))
        
        # Clear self junk cache to avoid performance issues
        import gc
        gc.collect()

    def get_last_processed_tracking(self):
        try:
            return ProcessingState.objects.get(key="last_processed_tracking").value
        except ProcessingState.DoesNotExist:
            return None

    def update_last_processed_tracking(self, tracking_number):
        state, created = ProcessingState.objects.get_or_create(key="last_processed_tracking")
        state.value = tracking_number
        state.save()