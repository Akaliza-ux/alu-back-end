#!/usr/bin/python3
"""
Gather data from an API.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    done_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"],
            len(done_tasks),
            len(todos)
        )
    )

    for task in done_tasks:
        print("\t {}".format(task["title"]))
        