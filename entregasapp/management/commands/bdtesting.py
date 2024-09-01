from entregasapp.models import bdoms

model_field_names = [field.name for field in bdoms._meta.get_fields()]

print(model_field_names)
