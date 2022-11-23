import csv
import os
from .tasks import * 

# hash for unfinished tasks.
todo_task_hash = {}
# keeps track of task ID's.
id_count = get_max_task() 

#small tests
task1 = Task(3, "some task")
todo_loader(todo_task_hash)
print(todo_task_hash)
print(id_count)

todo_cleaner(todo_task_hash, id_count);
