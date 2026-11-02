#!/usr/bin/python3
"""Gather data from an API and display an employee's TODO progress."""
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": user_id}).json()

    name = user.get("name")
    done = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
