#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_data = requests.get(user_url).json()
    username = user_data.get("username")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos = requests.get(todos_url).json()

    filename = "{}.csv".format(employee_id)

    with open(filename, "w") as file:
        for task in todos:
            line = '"{}","{}","{}","{}"\n'.format(
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            )
            file.write(line)

