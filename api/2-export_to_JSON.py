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

    completed_tasks = [task for task in todos if task.get('completed') is True]

    data = {user_id: [{"task": task.get('title'), "completed":
                task.get('completed'), "username": user.get('username')}
                for task in completed_tasks]}
    
    with open("{}.csv".format(user_id), "w", encoding='UTF8') as filename:
        json.dump(data, filename)
