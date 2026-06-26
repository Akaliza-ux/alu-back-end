#!/usr/bin/python3
"""Exports all employees TODO list data to a JSON file."""
import json
import requests


def export_all_employees_todo():
    """Fetch all employees tasks and export to JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(base_url))
    users = users_response.json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = "{}/todos".format(base_url)
        todos_response = requests.get(
            todos_url, params={"userId": user_id}
        )
        todos = todos_response.json()

        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_all_employees_todo()
    