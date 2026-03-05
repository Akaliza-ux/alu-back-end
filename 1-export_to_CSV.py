#!/usr/bin/python
import requests
import csv
import sys

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Get user info and TODOs
user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

# CSV filename
filename = f"{employee_id}.csv"

# Write CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for t in todos:
        writer.writerow([employee_id, user['username'], t['completed'], t['title']])
