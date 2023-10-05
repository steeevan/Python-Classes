import time


Filereader = open("sample.txt", "r")
fileContent = Filereader.read()

for line in Filereader:
    sentence = Filereader.readline()
    print(sentence)
Filereader.close()

time.sleep(4)
print("This is the file content",fileContent)