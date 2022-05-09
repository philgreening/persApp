import os
import sys
import django
import csv
# import xlsxwriter
from collections import defaultdict
from pathlib import Path


#sys.path.append('/home/philgreening/AWD_Midterm/proteinAPI')
sys.path.append('../../persApp/')


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'persApp.settings')
django.setup()

from persDb.models import *

# sequences_data_file =  '/home/philgreening/AWD_Midterm/proteinAPI/data/assignment_data_sequences.csv'
persData =  Path(__file__).parent / 'data/pers_data.txt'
print('file loaded...')


# variables to hold data

pers = defaultdict(list)


# Reads persData set csv file
with open(persData, encoding='utf8') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       next(csv_reader)
       lines = 0
       for row in csv_reader:
              pers[row[0]] = row[0:15]
       print('Pers - Check first row fields: ' + str(pers[row[0]]))
       print('file read...')

# clears database before database entries created
PeriodicalsOctavo.objects.all().delete()


# Variables to pass data to other models

pers_row = {}

print('data loading...')
# creates database entries in persoctavo model
for pers, data in pers.items():
       # try:
             
              row = PeriodicalsOctavo.objects.create(mms_id = data[1],
                                                 issn = data[2],
                                                 library_name = data[3],
                                                 new_library = data[4],
                                                 location_name = data[5],
                                                 new_location = data[6],
                                                 classmark = data[7],
                                                 new_per_number = data[8],
                                                 title = data[9],
                                                 holdings_and_wants = data[10],
                                                 new_holdings = data[11],
                                                 new_wants_and_notes = data[12],
                                                 labeled_on_shelf = data[13],
                                                 amended_on_alma = data[14],
              )

              row.save()
              pers_row[data[0]] = row





