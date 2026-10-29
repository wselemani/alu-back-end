#!/usr/bin/python3
"""Export all employees' tasks to a JSON file."""

import json
import requests


def fetch_data():
    """Fetch all users and their tasks from the API."""
    users_response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )

    if users_response.status_code != 200:
        return
    if todos_response.status_code != 200:
        return

    users = users_response.json()
    todos = todos_response.json()

    tasks_by_user = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        tasks_by_user[user_id] = []

        for todo in todos:
            if todo.get("userId") == user.get("id"):
                tasks_by_user[user_id].append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })

    return tasks_by_user


def main():
    """Save all employees' tasks to a JSON file."""
    tasks = fetch_data()
    if tasks is None:
        return

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks, json_file)


if __name__ == "__main__":
    main()
