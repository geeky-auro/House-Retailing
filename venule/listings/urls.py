from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='listings'),
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search'),
]

# listings/search 
# Note that the last url will be linked to the main method 