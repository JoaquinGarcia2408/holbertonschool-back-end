#!/usr/bin/python3
"""Shebang"""
import requests
from sys import argv
import csv


if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(user_url).json()

    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(user_id))
    todos = requests.get(todos_url).json()

    with open("{}.csv".format(user_id), "w", encoding='UTF8') as filename:
        writer = csv.writer(filename, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user["username"], task["completed"],
                            task["title"]])
