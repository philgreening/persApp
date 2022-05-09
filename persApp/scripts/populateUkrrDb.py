from operator import index
import os
import sys
import django
import csv
# import xlsxwriter
from collections import defaultdict
from pathlib import Path


sys.path.append('../../persApp/')


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'persApp.settings')
django.setup()

from persDb.models import *

persData =  Path(__file__).parent / 'data\All_Holdings_Offered3.csv'
print('file loaded...')


# variables to hold data

pers = defaultdict(list)

# Reads persData set csv file (remember to add numbered index column to inut file)
with open(persData, encoding='utf8') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       lines = 0
       line_count = 0
       for row in csv_reader:
            pers[row[0]] = row[0:28]
            line_count += 1

       print('Pers - Check first row fields: ' + str(pers[row[0]]))
       print('file read...')
       print(line_count)
       

# clears database before database entries created
PeriodicalsUKRRStatus.objects.all().delete()

# Variables to pass data to other models

pers_row = {}

print('data loading...')

#creates an entry into the UKRR pers database

counter = 0
for pers, data in pers.items():

       # try:
       counter  += 1
       row = PeriodicalsUKRRStatus.objects.create(library_code = data[1],
                                        cycle_name = data[2],
                                        cycle_list_name = data[3],
                                        UKRR_id = data[4],
                                        issn = data[5],
                                        title = data[6],
                                        offering = data[7],
                                        supplements = data[8],
                                        gaps = data[9],
                                        shelf_space = data[10],
                                        scarcity = data[11],
                                        holding = data[12],
                                        overlap = data[13],
                                        bl_scarcity = data[14],
                                        bl_scarcity_date = data[15],
                                        ml_scarcity = data[16],
                                        ml_scarcity_date = data[17],
                                        bl_response = data[18],
                                        not_requested = data[19],
                                        holdings_requested = data[20],
                                        date_of_request = data[21],
                                        bl_return_ref = data[22],
                                        bl_overlap = data[23],
                                        retention_status = data[24],
                                        transfer_to_bl = data[25],
                                        retain = data[26],
                                        dispose = data[27],
       )
       row.save()
       pers_row[data[0]] = row

print(counter)







