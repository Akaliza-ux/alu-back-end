#!/usr/bin/python3
"""
Gather data from an API.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get employee information
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    user = user_response.json()

    # Get employee TODO list
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    )
    todos = todo_response.json()

    employee_name = user["name"]
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task["completed"]]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
        