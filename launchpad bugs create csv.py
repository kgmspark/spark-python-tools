# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:09:05 2023

@author: direc
"""

import csv  
from csv import DictWriter


from launchpadlib.launchpad import Launchpad


pailsbugs = [
    1736565,
    2024610,
    1667080,
    2024482,
    1989368,
]

field_names = ['number', 'title', 'status', 'target', 'heat', 'tags']

with open("bugs.csv", "a", newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writeheader()
        f_object.close()

launchpad = Launchpad.login_anonymously('just testing', 'production', version='devel') 

for row in pailsbugs :
    
    bug_one = launchpad.bugs[row]
    tasks = bug_one.bug_tasks
    bugid = (bug_one.id)
    title = (bug_one.title)
    heat = (bug_one.heat)
    for task in tasks:
        milestonelink = str(task.milestone)
        status = (task.status)
        tags = (bug_one.tags)
        milestone = (milestonelink.split('/')[-1])


    dict = {'number': bugid, 'title': title, 'status': status, 'target': milestone, 'heat' : heat, 'tags': tags}

    with open("bugs.csv", "a", newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        f_object.close()

