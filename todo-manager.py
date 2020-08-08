#!/usr/bin/env python3

from termcolor import colored
import os
import json
import datetime

tasksList = {}


def listTasks():
    loadFromFile()
    try:
        if len(tasksList) != 0:
            for key, value in tasksList.items():
                print(colored(key, "yellow"), colored(value, "blue"))
        else:
            print(colored("Tasks is empty.", "yellow"))
    except ValueError:
        print(colored("Valuerror.....", "red"))


def addTask():
    new_task = str(input("Enter new task name: "))
    if isinstance(new_task, str) and not "":
        try:
            tasksList[len(tasksList)] = new_task
            print(colored("Task is added.", "green"))
        except ValueError:
            print("ValueError")
    else:
        print("not a string")


def deleteTask():
    listTasks()
    if len(tasksList) != 0:
        try:
            delete_task = int(input("Enter delete task number: "))
            if delete_task in tasksList:
                del tasksList[delete_task]
                print(colored("Task is deleted.", "green"))
        except ValueError:
            print("ValueError")


def editTask():
    listTasks()
    if len(tasksList) != 0:
        try:
            edit_task = int(input("Enter edit task number: "))
            print("******")
            if edit_task in tasksList.keys():
                edited_task = input("Enter the new task: ")
                tasksList[edit_task] = edited_task
                print(colored("Task is changed.", "green"))
        except ValueError:
            print(colored("Cannot edit the task number you have entered.", "red"))


def saveToFile():
    try:
        file_path = os.path.expanduser('todo-save.json')
        with open(file_path, 'w+') as json_file:
            json_file.truncate()
            json.dump(tasksList, json_file)
            print(colored("File is saved!", "yellow"))
    except IOError:
        print(colored("File not accessible", "red"))


def loadFromFile():
    file_path = os.path.expanduser('todo-save.json')
    try:
        with open(file_path) as json_file:
            json.load(json_file)
    except IOError:
        print(colored("File failed to load.", "red"))


def main():
    while True:
        print("1) Add Task", "2) Delete Task", "3) List Tasks", "4) Edit Task", "0) Exit", sep="\n")

        action = input("Choose an option: ")
        try:
            if int(action) in performAction.keys():
                # loadFromFile()
                performAction.get(int(action))()
            elif int(action) == 0:
                saveToFile()
                break
            else:
                print("Pleae input valid option.")

        except ValueError:
            print(colored("ValueError....", "red"))


performAction = {1: addTask, 2: deleteTask, 3: listTasks, 4: editTask}

if __name__ == '__main__':
    main()
