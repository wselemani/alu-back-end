#!/usr/bin/python3
"""Export an employee's tasks to a CSV file."""

import csv
import requests
import sys


def main():
    """Fetch employee tasks and save them to a CSV file."""
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

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
