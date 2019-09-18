#Open an existing file
# f = open("demofile.txt", "r")

##Read the whole file
#print(f.read())

##Read only parts of the file (5 first characters)
#print(f.read(5))

##Read one line of the file
# print(f.readline()) 

##Read two lines of the file
# print(f.readline())
# print(f.readline())

##Read the whole file line by line
# for x in f:
#     print(x)
#     
# f.close()

##Create a new file and write in it
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()
# 
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

##Overwrite the content
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
# 
# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read()) 

# #Create a new file
# f = open("myfile.txt", "x")

# #Create a new file if it doesn't exists
# f = open("myfile.txt", "w")

#Remove files
import os
# os.remove("myfile.txt")

#Check if file exist before deleting
# if os.path.exists("demofile3.txt"):
#     os.remove("demofile3.txt")
#     print("File removed sucessfully") 
# else:
#     print("The file does not exist")

#Remove a whole folder
os.rmdir("folderdemo")
    
    

