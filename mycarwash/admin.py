from django.contrib import admin
from .models import (
    CarModel,
    SelectionServices,
    RequestUser
)
# Register your models here.

admin.site.register(CarModel)
admin.site.register(SelectionServices)
admin.site.register(RequestUser)
