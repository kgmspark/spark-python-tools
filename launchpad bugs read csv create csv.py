# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:09:05 2023

@author: kgmspark
"""

import csv  
from csv import DictWriter
from launchpadlib.launchpad import Launchpad



# Top-level parameters
# The output file
outfilename = 'ourbugs091925-out.csv'
infilename = 'ourbugs091925.csv'


# This is a list of all supported column names in the CSV
field_names = ['number', 'title',  'heat', 'tags', 'comments', 'status', 'target', 'url']

# Open the output file
# The reason for needing to specify the newline is to apologize for Windows
# You see, Windows is the only OS in common use that stupidly appends \n\r
# (newline AND carriage return) to the end of every line. Other systems (and
# apparently Excel) naively interpret this as TWO new lines.  We can stop this
# entire nonsense by forcing Python to only insert \n instead.
with open(outfilename, "w", newline='\n') as fout:
    # Open the launchpad interface to download the bug metadata
    launchpad = Launchpad.login_anonymously('just testing', 'production', version='devel')
    # The dict writer will be used to construct the CSV output file line-by-line
    dictwriter_object = DictWriter(fout, fieldnames=field_names)
    # First, we'll write the header
    dictwriter_object.writeheader()
    # Start parsing the input file
    # The input is required to be a CSV with a column called 'bug' with integer values
    with open(infilename, 'r') as ourbugs:
        reader = csv.DictReader(ourbugs)
        for row in reader:
            # Go get the bug from Launchpad
            bug = launchpad.bugs[row['bug']]
            # Tell the user what we're up to
            print(bug.title)
            # This is an awkward way to grab only the last task
            # Crunch through all the tasks and exit the loop on the last one
            for task in bug.bug_tasks:
                pass
            # The milestone is a link - let's grab the last part of the URL
            milestonelink = str(task.milestone)
            milestone = milestonelink.split('/')[-1]
            # NOTE!  If you decide to report multiple tasks in the future,
            #    you'll also need to grab the task.status in the loop.  Right now,
            #    it isn't grabbed until the dictionary below.
            # Build the row as a dictionary.
            thisrow = {
                'number': bug.id,
                'title': bug.title,
                'status': task.status,
                'target': milestone,
                'heat' : bug.heat,
                'tags': bug.tags,
                'comments': bug.message_count,
                'url' : bug.web_link}
            # Write it
            dictwriter_object.writerow(thisrow)


