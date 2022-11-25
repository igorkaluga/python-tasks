import csv
import os
from prettytable import PrettyTable
from .tasks import * 
from .modules.task_actions import *

# hash for unfinished tasks.
todo_task_hash = {}
# keeps track of task ID's.
id_count = get_max_task() 

# runs task loader to lead tasks from csv and stores them into todo_task_hash.
todo_loader(todo_task_hash)

# cli cleaner
clear = lambda: os.system("clear")

run_tasks = True
# REPL for imput
while run_tasks:
    print("\nType 'Q' to quit.")
    print("Type 'F' to finish a task.\n")

    """ A REPL for task input """
    # display current tasks
    table = PrettyTable(["Task ID", "Task Name", "Status"])
    for task in todo_task_hash:
        task_arr = todo_task_hash[task]
        table.add_row([task_arr[0], task_arr[1], task_arr[2]])
    print(table)
    # task prompt
    # asks for task name.
    user_task = input("\nEnter task name: \n")
    if user_task == "q" or user_task == "Q":
        #quits loop
        run_tasks = False
        # run todo_cleaner on quit
        #todo_cleaner(todo_task_hash, id_count);
        clear()
        break
    if user_task == "f" or user_task == "F":
        # updates task status to complete
        update_task_id = input("Enter task id: \n")
        todo_task_hash[int(update_task_id)][2] = "TRUE" 
        clear()
        continue
    
    id_count += 1

    new_task = Task(id_count, user_task);
    todo_task_hash[new_task.task_id] = [new_task.task_id, new_task.task_name, new_task.status]
    clear()

todo_cleaner(todo_task_hash, id_count);
