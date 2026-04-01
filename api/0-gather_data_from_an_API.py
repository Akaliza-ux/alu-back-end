#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    user_response = requests.get(user_url)
    employee_name = user_response.json().get("name")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    todos = requests.get(todos_url).json()

    total_tasks = len(todos)
    done_titles = []

    for task in todos:
        if task.get("completed"):
            done_titles.append(task.get("title"))

print("Employee {} is done with tasks({}/{})".format(employee_name, len(done_titles), total_tasks))
    
for title in done_titles:
        print("\t {}".format(title))


