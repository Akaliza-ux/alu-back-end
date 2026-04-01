#!/usr/bin/python3
import requests
import sys
import json

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_data = requests.get(user_url).json()
    username = user_data.get("username")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos = requests.get(todos_url).json()

    tasks_list = []

    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    result = {employee_id: tasks_list}

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as file:
        json.dump(result, file)

