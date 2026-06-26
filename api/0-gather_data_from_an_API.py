#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get employee information
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    # Get employee TODO list
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
        