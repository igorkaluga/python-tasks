import os
import csv

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Task():
    """
        Main class for a task. 
    """ 

    def __init__(self, task_id, task_name):
        self.task_id = task_id
        self.task_name = task_name
        self.status = "FALSE";

    def append_task(self):
        with open(os.path.join(__location__, "logs/todo_tasks.csv"), "a", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([self.task_id, self.task_name, self.status])

def todo_loader(task_hash):
    """ Loads unfinished tasks from todo_tasks.csv file on startup. """
    with open(os.path.join(__location__, "logs/todo_tasks.csv"), "r", encoding="UTF8") as todo_read:
        reader = csv.reader(todo_read)

        for row in reader:
            if row[0] == "TASK_ID" or row[0] == "MAX_TASK_ID":
                continue
            if row[2] == "FALSE":
                task_hash[row[0]] = row

def get_max_task():
    """ Gets the max task number to use for further task # incrementation """
    with open(os.path.join(__location__, "logs/todo_tasks.csv"), "r", encoding="UTF") as f:
        reader = csv.reader(f)

        for row in reader:
            if row[0] == "MAX_TASK_ID":
                return row[1]
                break


def todo_cleaner(task_hash, max_task_num):
    """ Cleans up the todo_tasks.csv list by rewriting it to only have unfinished taks. """
    with open(os.path.join(__location__, "logs/todo_tasks.csv"), "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        header = ["TASK_ID", "TASK_NAME", "STATUS"]
        max_num = ["MAX_TASK_ID", max_task_num]
        #use writerows instead.
        writer.writerow(header)
        writer.writerow(max_num)
        
        for obj_key in task_hash:
            if task_hash[obj_key][2] == "FALSE":
                writer.writerow(task_hash[obj_key])
