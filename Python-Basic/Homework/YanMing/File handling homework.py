#Question 1
try:
    userinput = input("What do you want to write? ")
    file1 = open("myfile.txt", "w")
    file1.write(userinput)
    file1.close()
except:
    print("Something went wrong")
#Question 2
try:
    file2 = open("sample.txt", "r")
    print(file2.read())
    file2.close()
except:
    print("Something went wrong")
