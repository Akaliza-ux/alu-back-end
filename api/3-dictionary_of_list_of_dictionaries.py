#!usr/bin/python3
import requests
import json

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()

    result = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
        todos = requests.get(todos_url).json()

        tasks_list = []

        for task in todos:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        result[user_id] = tasks_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(result, file)

