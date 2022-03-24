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
persData =  Path(__file__).parent / 'data\All_Holdings_Offered.csv'
print('file loaded...')


# variables to hold data

pers = defaultdict(list)


# Reads protein set csv file
with open(persData, encoding='utf8') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       lines = 0
       line_count = 0
       for row in csv_reader:
            pers[row[0]] = row[0:27]
            line_count += 1

       print('Pers - Check first row fields: ' + str(pers[row[0]]))
       print('file read...')
       print(line_count)
       

# clears database before database entries created
PeriodicalsUKRRStatus.objects.all().delete()

# Variables to pass data to other models

pers_row = {}

print('data loading...')
# creates database entries in protein model
for pers, data in pers.items():

       #if unable to match sequence data to protein_id, Null is added to sequence
       # try:
       row = PeriodicalsUKRRStatus.objects.create(library_code = data[0],
                                        cycle_name = data[1],
                                        cycle_list_name = data[2],
                                        UKRR_id = data[3],
                                        issn = data[4],
                                        title = data[5],
                                        offering = data[6],
                                        supplements = data[7],
                                        gaps = data[8],
                                        shelf_space = data[9],
                                        scarcity = data[10],
                                        holding = data[11],
                                        overlap = data[12],
                                        bl_scarcity = data[13],
                                        bl_scarcity_date = data[14],
                                        ml_scarcity = data[15],
                                        ml_scarcity_date = data[16],
                                        bl_response = data[17],
                                        not_requested = data[18],
                                        holdings_requested = data[19],
                                        date_of_request = data[20],
                                        bl_return_ref = data[21],
                                        bl_overlap = data[22],
                                        retention_status = data[23],
                                        transfer_to_bl = data[24],
                                        retain = data[25],
                                        dispose = data[26],
       )
       row.save()
       pers_row[data[0]] = row





