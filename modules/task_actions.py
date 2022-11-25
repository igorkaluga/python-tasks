import os
import csv

#__location__ = os.path.realpath(
#        os.path.join(os.getcwd(), os.path.dirname(__file__)))

__location__ = os.path.dirname(os.path.dirname(__file__))

def todo_loader(task_hash):
    """ Loads unfinished tasks from todo_tasks.csv file on startup. """
    with open(os.path.join(__location__, "logs/todo_tasks.csv"), "r", encoding="UTF8") as todo_read:
        reader = csv.reader(todo_read)

        for row in reader:
            if row[0] == "TASK_ID" or row[0] == "MAX_TASK_ID":
                continue
            if row[2] == "FALSE":
                task_hash[int(row[0])] = row

def get_max_task():
    """ Gets the max task number to use for further task # incrementation """
    with open(os.path.join(__location__, "logs/todo_tasks.csv"), "r", encoding="UTF") as f:
        reader = csv.reader(f)

        for row in reader:
            if row[0] == "MAX_TASK_ID":
                return int(row[1])
                break


def todo_cleaner(task_hash, max_task_num):
    """ Cleans up the todo_tasks.csv list by rewriting it to only have unfinished taks. """
    with open(os.path.join(__location__, "logs/todo_tasks.csv"), "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        header = [["TASK_ID", "TASK_NAME", "STATUS"],
                  ["MAX_TASK_ID", max_task_num]]
        writer.writerows(header)
        
        for obj_key in task_hash:
            if task_hash[obj_key][2] == "FALSE":
                writer.writerow(task_hash[obj_key])
