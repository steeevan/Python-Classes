UserPrompt =  input('Enter a name for the file ' )
UserContentPrompt = input("Enter the content for that file ")




UserFile = open(UserPrompt, "w")
UserFile.write(UserContentPrompt)
UserFile.close()
print("Sucess! Check your Finder/File Explorer.")