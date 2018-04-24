#!/usr/bin/env python3

import os
import csv
from run_cache import RunCache
from caesar import CaesarClient

USERNAME = os.environ["PANOPTES_USERNAME"]
PASSWORD = os.environ["PANOPTES_PASSWORD"]
WORKFLOW_ID = 5374

last_run = RunCache('last_run.pickle')
caesar = CaesarClient(USERNAME, PASSWORD)

with open("scores_with_gold.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        subject_id = int(row[0])
        gold = int(row[1])
        score = float(row[2])
        
        if last_run.is_changed(subject_id, row):
            last_run.update(subject_id, row)
            data = {'gold': gold, 'score': score}
            r = caesar.update_reduction(WORKFLOW_ID, subject_id, data)

            if not r.status_code == 200:
                print(r.text)
            else:
                print("OK %i" % subject_id)
                

last_run.save()
