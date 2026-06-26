#!/usr/bin/python3
"""Exports employee TODO list data to a CSV file."""
import csv
import requests
import sys


def export_employee_todo_csv(employee_id):
    """Fetch employee tasks and export to CSV file."""
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

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    export_employee_todo_csv(employee_id)
    