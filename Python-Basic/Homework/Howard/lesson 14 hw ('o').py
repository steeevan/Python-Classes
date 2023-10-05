#  PROBLEM...1

file_name = input("Create the name of your file: ")
file_content = input("Add the content of your file: ")
file1 = open(file_name,"w")
file1.write(file_content)
file1.close()
print(file_name,"has been sucssesfully created (O_O)")
print("the contents is...",file_content,"!!!")


#  PROBLEM...

file2 = open("sample.txt","r")
content = file2.read()
print("THE CONTENTS OF SAMPLE.TXT IS...")
print(content)
file2.close()
