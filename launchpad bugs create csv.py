# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:09:05 2023

@author: direc
"""
#you will need to list the launchpad bugs you want to report on in the 'ourbugs' variable below
import csv  
from csv import writer


from launchpadlib.launchpad import Launchpad


ourbugs = [
    1736565,
    2024610,
    1667080,
    2024482,
    1989368,
    1837799,
]

launchpad = Launchpad.login_anonymously('just testing', 'production', version='devel') 

for row in ourbugs :
    
    bug_one = launchpad.bugs[row]
    tasks = bug_one.bug_tasks
    bugid = (bug_one.id)
    title = (bug_one.title)
    for task in tasks:
        milestonelink = str(task.milestone)
        status = (task.status)
        tags = (bug_one.tags)
        milestone = (milestonelink.split('/')[-1])

    header = ['number', 'title', 'status', 'target', 'tags']

    data = [bugid, title, status, milestone, tags]

    with open("temp.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(header)
        writer.writerow(data)
        stream.close()
