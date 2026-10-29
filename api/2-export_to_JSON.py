#!/usr/bin/python3
"""Export an employee's tasks to a JSON file."""

import json
import requests
import sys


def main():
    """Fetch employee tasks and save them to a JSON file."""
    if len(sys.argv) != 2:
        return

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(
        "{}/users/{}".format(base_url, user_id)
    )
    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": user_id}
    )

    if user_response.status_code != 200:
        return
    if todos_response.status_code != 200:
        return

    username = user_response.json().get("username")
    tasks = todos_response.json()

    employee_tasks = []
    for task in tasks:
        employee_tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({user_id: employee_tasks}, json_file)


if __name__ == "__main__":
    main()
