#!/usr/bin/env python3

import os
import sys
import csv
from run_cache import RunCache
from caesar import CaesarClient

USERNAME = os.environ["PANOPTES_USERNAME"]
PASSWORD = os.environ["PANOPTES_PASSWORD"]
WORKFLOW_ID = 5374

last_run = RunCache('last_run.pickle')
caesar = CaesarClient(USERNAME, PASSWORD)

csv_filename = sys.argv[1]

with open(csv_filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        subject_id = int(row['id'])
        
        if last_run.is_changed(subject_id, row):
            last_run.update(subject_id, row)
            last_run.save()
            data = {
                'gold': int(row['gold']),
                'score': float(row['score']),
                'retired': int(row['retired']),
                'seen': int(row['seen'])
            }
            r = caesar.update_reduction(WORKFLOW_ID, subject_id, data)

            if not r.status_code == 200:
                print(r.text)
            else:
                print("OK %i" % subject_id)
                

last_run.save()
