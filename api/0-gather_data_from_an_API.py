#!/usr/bin/python3
"""Fetch TODO list"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display employee TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)
    employee_name = user_response.json().get("name")

    # Fetch todos
    todos_response = requests.get(
        f"{base_url}/todos",
        params={"userId": employee_id}
    )
    todos = todos_response.json()

    total = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_done = len(done_tasks)

    # Display
    print(
        "Employee {} is done with tasks({}/{}):".format(
        employee_name,
        number_done,
        total
        )
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
