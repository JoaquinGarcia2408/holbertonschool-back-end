#!/usr/bin/python3
"""Shebang"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url).json()

    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(user_id))
    todos = requests.get(todos_url).json()

    user_task = {}

    for user in users:
        data = [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user["username"]
                }
                for task in todos if user["id"] == task["userId"]
            ]
        user_task[user["id"]] = data

        with open("todo_all_employees.json", 'w', encoding='UTF=8') as f:
            json.dump(user_task, f)
