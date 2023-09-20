from django.contrib import admin

# Register your models here.
from .models import Realtors
from .models import Listings

admin.site.register(Realtors)
admin.site.register(Listings)