def display_menu():
  print("To-Do List Manager")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. View Task")
  print("4. Exit")

def add_task(tasks):
  task = input("Enter the task: ")
  tasks.append(task)
  print("Task added successfully!")

def remove_task(tasks):
  task_pos = int(input("Enter the index of the task to remove: "))
  if 1<= task_pos <= len(tasks):
    removed_task = tasks.pop(task_index - 1)
    print(f"Task '{removed_task}' removed successfully!")
  else:
    print("Invalid Position Entered!")
    
def view_task(tasks):
  if tasks:
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
      print(f"{index}. {task}")
    
  else:
    print("No tasks to display!")
