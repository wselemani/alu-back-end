#!/usr/bin/python3
"""Gather an employee's TODO list from an API."""

import sys

import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Print an employee's completed tasks."""
    employee_id = sys.argv[1]

    user_url = "{}/users/{}".format(BASE_URL, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_url = "{}/todos".format(BASE_URL)
    todos_response = requests.get(todos_url)
    all_todos = todos_response.json()

    employee_todos = [
        todo for todo in all_todos
        if todo.get("userId") == int(employee_id)
    ]

    completed_tasks = [
        todo for todo in employee_todos
        if todo.get("completed")
    ]

    total_tasks = len(employee_todos)
    number_completed = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_completed, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
