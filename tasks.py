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

