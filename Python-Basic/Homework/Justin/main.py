t=0
a={}
while t != 4: 
  print("                       ")
  print("1: make a task")
  print("2: veiw tasks")
  print("3: mark a task")
  print("4:quit")
  print("                       ")
  t=int(input("What do you want to do? chose one: 1 2 3 4:  "))
  
  if t == 1:
    a[1] = input("what is the name of the task")
    a[2] = input("what is the description")
    a[3] = ("not compleated")
  elif t == 2:
    print(a)
  elif t == 3:
    a[3] = ("compleated")
    print("Marked as compleat")
print("                         ")
print("bye")