#!/usr/bin/python
import requests
import json

# Get all users and todos
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

# Prepare dictionary
user_dict = {str(user['id']): [] for user in users}

for t in todos:
    user_id = str(t['userId'])
    username = next(u['username'] for u in users if u['id'] == t['userId'])
    user_dict[user_id].append({
        "username": username,
        "task": t['title'],
        "completed": t['completed']
    })

# Write JSON file
with open("todo_all_employees.json", "w") as f:
    json.dump(user_dict, f)
