from django.contrib import admin
from .models import *

class PeriodicalsOctavoAdmin(admin.ModelAdmin):
    list_display = [
        'mms_id', 'issn', 'library_name',
         'new_library', 'location_name',
         'new_location', 'classmark', 'new_per_number',
         'title', 'holdings_and_wants', 'new_holdings',
         'new_wants_and_notes', 'labeled_on_shelf', 'amended_on_alma'
    ]

admin.site.register(PeriodicalsOctavo, PeriodicalsOctavoAdmin)
    
