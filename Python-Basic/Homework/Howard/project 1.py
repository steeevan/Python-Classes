tasks = []
quit_or_not = 0
while quit_or_not == 0:
 print("                  ")
 print("To do list manager")
 print("1. add task")
 print("2. view task")
 print("3. mark task as complete")
 print("4. quit")

 p = {}
 w = int(input("pick 1, 2, 3, or 4: "))
 if w == 1:
  k = (input("enter a task title: "))
  p["task_title"] = k
 
  t = (input("enter a task description: "))
  p["task_description"] = t
  p["status"] = "incomplete" 
  tasks.append(p)
  print("tasks '",k,"' added successfully!😄")
  
 elif w == 2:
   print("tasks:")
   c = 1
   for m in tasks:  
    print(c,"title:",m["task_title"])
    print("  description:",m["task_description"])
    print("  status:",m["status"])
    c += 1
 
 elif w == 3:
   dohicky = int(input("Enter the task number to mark as complete: "))
   p = tasks[dohicky - 1]
   p["status"] = "complete"
   print("Task",p["task_title"],"marked as complete!😊")
 
 elif w == 4:
  quit_or_not = 1 
  print("goodbye👋")
 
 else:
    print("something went wrong")
