#!/usr/bin/python3
"""Shebang"""
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

    completed_tasks = [task.get('title') for task in todos
                       if task.get('completed') is True]
     print(f"Employee {user['name']} is done with tasks"
          f"({completed}/{not_completed + completed}):")
    for task in user_todo:
        if task["completed"]:
            print(f'\t {task["title"]}')
