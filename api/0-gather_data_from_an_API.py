#!/usr/bin/python
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Get employee info
user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
user = requests.get(user_url).json()

# Get TODOs
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
todos = requests.get(todos_url).json()

# Filter completed tasks
done_tasks = [t for t in todos if t['completed']]

# Print output in required format
print(f"Employee {user['name']} is done with tasks({len(done_tasks)}/{len(todos)}):")
for task in done_tasks:
    print("\t", task['title'])
