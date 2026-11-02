#!/usr/bin/python3
"""Export an employee's TODO data to CSV."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": user_id}).json()

    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
