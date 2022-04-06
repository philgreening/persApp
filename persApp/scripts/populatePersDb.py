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
persData =  Path(__file__).parent / 'data\per1.txt'
print('file loaded...')


# variables to hold data

pers = defaultdict(list)


# Reads protein set csv file
with open(persData, encoding='utf8') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       lines = 0
       for row in csv_reader:
              pers[row[0]] = row[0:14]
       print('Protein - Check first row fields: ' + str(pers[row[0]]))
       print('file read...')

# clears database before database entries created
PeriodicalsOctavo.objects.all().delete()


# Variables to pass data to other models

pers_row = {}

print('data loading...')
# creates database entries in protein model
for pers, data in pers.items():
       #if unable to match sequence data to protein_id, Null is added to sequence
       # try:
             
              row = PeriodicalsOctavo.objects.create(mms_id = data[0],
                                                 issn = data[1],
                                                 library_name = data[2],
                                                 new_library = data[3],
                                                 location_name = data[4],
                                                 new_location = data[5],
                                                 classmark = data[6],
                                                 new_per_number = data[7],
                                                 title = data[8],
                                                 holdings_and_wants = data[9],
                                                 new_holdings = data[10],
                                                 new_wants_and_notes = data[11],
                                                 labeled_on_shelf = data[12],
                                                 amended_on_alma = data[13],
              )

              row.save()
              pers_row[data[0]] = row





