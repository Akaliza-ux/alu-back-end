#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display employee TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee with ID {} not found.".format(employee_id))
        sys.exit(1)
    employee_name = user_response.json().get("username")

    todos_url = "{}/todos".format(base_url)
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    total = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total
    ))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


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
    