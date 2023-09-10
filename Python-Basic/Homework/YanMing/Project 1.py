tasknumber = 0
userinput = 0
dic = {"Task title:":"","Task description:":""}
lst = []
lstt = []
lsttt = []
task_title = ""
task_description = ""
status = "Incomplete"
def mainmenu():
  print("Welcome to the main menu.")
  print("What would you like to do?")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task as Complete")
  print("4. Quit")
def tasks():
  print(f"The ones that are complete is task {lsttt}")


while userinput != 4:
  mainmenu()
  userinput = int(input("Enter your choice."))
  if userinput == 1:
    task_title = input("Enter task title:")
    task_description = input("Enter task description:")
    keys = dic["Task title:"] = task_title
    values = dic["Task description:"] = task_description
    lst.append(keys)
    lstt.append(values)
    print(f"Task {dic} added sucessfully!")
  elif userinput == 2:
    print(f"Title: {lst}")
    print(f"Description: {lstt}")
    tasks()
  elif userinput == 3:
    tasknumber = int(input("What task to mark as complete?"))
    lsttt.append(tasknumber)
    print("Task", lst[tasknumber], "marked as complete!")
  elif userinput == 4:
    print("Exiting...")
  else:
    print("Invalid Input.")
