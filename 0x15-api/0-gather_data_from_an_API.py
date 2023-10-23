#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
- Returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done witih tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]