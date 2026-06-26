#!/usr/bin/python3
"""Exports employee TODO list data to a JSON file."""
import json
import requests
import sys


def export_employee_todo_json(employee_id):
    """Fetch employee tasks and export to JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee with ID {} not found.".format(employee_id))
        sys.exit(1)
    username = user_response.json().get("username")

    todos_url = "{}/todos".format(base_url)
    todos_response = requests.get(
        todos_url, params={"userId": employee_id}
    )
    todos = todos_response.json()

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    export_employee_todo_json(employee_id)
    