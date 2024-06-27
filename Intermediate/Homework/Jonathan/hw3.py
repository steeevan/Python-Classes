import tkinter as tk
root=tk.Tk()

user_label=tk.Label(root ,text="username")
pass_label=tk.Label(root ,text="Password")

user_label.grid(row=1,column=1,padx=10,pady=10)
user_label.grid(row=2,column=1,padx=10,pady=10)

entry_user=tk.Entry(root)
entry_pass=tk.Entry(root)


def get_input():
  user=entry_user.get()
  passw=entry_pass.get()
  print(user)
  print(passw)

print_button=tk.Button(root,text="print", command=get_input)
print_button.grid(row=2,column=1,padx=5,pady=5)

'''
had trouble with the code
'''
