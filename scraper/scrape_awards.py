#!/usr/bin/env python

import csv
from collections import defaultdict
import json

import requests

def check_link(link):
  """
  Check a single link.
  """
  try:
    r = requests.get(link, allow_redirects=False)
    print "(%s) %s" % (r.status_code, link)
    return r.status_code

  except:
    print "(timeout) %s" % link
    return "timeout"

def read_csv(path):
  """
  Reads a CSV file into a list of dicts.
  """
  with open(path, 'r') as readfile:
    return list(csv.DictReader(readfile))

if __name__ == "__main__":
  """
  GROUND CONTROL TO MAJOR TOM.
  """

  report = defaultdict(int)
  results = []

  for row in read_csv('ONA-Finalists-All-Cleaned-csv.csv'):
    status_code = check_link(row['Url'])
    report[status_code] += 1
    row['linkStatus'] = status_code
    results.append(row)

  with open('report.json', 'w') as writefile:
    writefile.write(json.dumps(report))

  with open('results.json', 'w') as writefile:
    writefile.write("results=%s" % json.dumps(results))