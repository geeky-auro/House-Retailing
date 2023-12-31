from django.contrib import admin

# Register your models here.
from .models import Listing



class ListingAdmin(admin.ModelAdmin):
    # Now we need to define what we can have in the table
    list_display=('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    # To have a filter box ;)
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title','description','address','city','state','zipcode','price')
    list_per_page=25

admin.site.register(Listing,ListingAdmin)