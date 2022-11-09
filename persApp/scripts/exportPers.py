import os
import sys
import django
import csv

from collections import defaultdict
from pathlib import Path

sys.path.append('../../persApp/')


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'persApp.settings')
django.setup()

from persDb.models import *

pers = PeriodicalsOctavo.objects.all()

with open('pers_export.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
                        'mms_id', 
                        'issn', 
                        'library_name',
                        'new_library',
                        'location_name',
                        'new_location',
                        'classmark',
                        'new_per_number',
                        'title',
                        'holdings_and_wants',
                        'new_holdings',
                        'new_wants_and_notes',
                        'labeled_on_shelf',
                        'amended_on_alma'
                        ])
    pers_fields = pers.values_list(
                        'mms_id', 
                        'issn', 
                        'library_name',
                        'new_library',
                        'location_name',
                        'new_location',
                        'classmark',
                        'new_per_number',
                        'title',
                        'holdings_and_wants',
                        'new_holdings',
                        'new_wants_and_notes',
                        'labeled_on_shelf',
                        'amended_on_alma'
                        )
    for pers in pers_fields:
        writer.writerow(pers)

