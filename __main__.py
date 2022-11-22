import csv
import os

# assigns package path as __location__
__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

test_header = ["t_id", "t_name"]
test_data = ["1", "edit csv file"]
test_data2 = ["2", "another task"]

class csv_editor():
    

# writer
with open(os.path.join(__location__, "logs/tasks.csv"), "w", encoding="UTF8", newline="") as todo_file:
    writer = csv.writer(todo_file)

    writer.writerow(test_header)

    writer.writerow(test_data2)

# reader
with open(os.path.join(__location__, "logs/tasks.csv"), "r", encoding="UTF8") as todo_read:
    reader = csv.reader(todo_read)

    for row in reader:
        print(row)
