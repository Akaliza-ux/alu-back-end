#!/usr/bin/python
import requests
import json
import sys

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Get user info and TODOs
user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()

# Prepare JSON data
data = {
    employee_id: [{"task": t['title'], "completed": t['completed'], "username": user['username']} for t in todos]
}

# Write JSON to file
with open(f"{employee_id}.json", "w") as f:
    json.dump(data, f)
