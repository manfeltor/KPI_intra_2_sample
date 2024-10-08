# yourapp/management/commands/check_tracking_availability.py
import requests
import json
import re
from django.core.management.base import BaseCommand
from entregasapp.models import bdoms
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
CAKEY = config('CAKEY')
CAAGREEMENT = config('CAAGREEMENT')
CATRKURL = config('CATRKURL')

class Command(BaseCommand):
    help = 'Check the availability of tracking data starting from the oldest date'

    API_URL = CATRKURL
    HEADERS = {
        "authorization": CAKEY,
        "agreement": CAAGREEMENT,
    }
    VALID_TRACKING_REGEX = re.compile(r'^19.{16}$')  # Adjust the length as needed

    def handle(self, *args, **kwargs):
        # Fetch tracking numbers from bdoms and filter with regex
        tracking_numbers = list(
            bdoms.objects.filter(trackingTransporte__isnull=False)
            .order_by('fechaCreacion')
            .values_list('trackingTransporte', flat=True)
            .distinct()
        )
        
        # Filter tracking numbers with regex
        valid_tracking_numbers = [tn for tn in tracking_numbers if self.VALID_TRACKING_REGEX.match(tn)]

        if not valid_tracking_numbers:
            self.stdout.write(self.style.WARNING("No valid tracking numbers found in bdoms."))
            return

        # Check availability starting from the oldest
        batch_size = 20
        for i in range(0, len(valid_tracking_numbers), batch_size):
            batch = valid_tracking_numbers[i:i + batch_size]
            if not batch:
                break

            parameters = {
                "extClient": "",
                "trackingNumbers": batch
            }
            try:
                response = requests.get(self.API_URL, headers=self.HEADERS, params=parameters)
                response.raise_for_status()
                data = response.json()

                available_dates = [tn for tn in batch if any(event.get('trackingNumber') == tn for event in data)]
                if available_dates:
                    self.stdout.write(self.style.SUCCESS(f"Available data found for dates: {available_dates}"))
                    break
                else:
                    self.stdout.write(self.style.WARNING(f"No available data for batch: {batch}"))
            except requests.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Request failed for batch {batch}: {e}"))
                return
