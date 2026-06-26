#!/usr/bin/python3
"""Gather data from an API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(done_tasks),
            len(todos)
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
        