# opening a file and reading the file content

#file = open("example.txt", 'r')

# content = file.read()

#redirects the pointer to the first item in the list
# file.seek(0)
#
# content = file.readlines()
#
# print(content)
#
# file.close()

#writing content to a text file

#creating file
#w method only adds one line of text - it does not append
# file = open("example2.txt", 'w')
# file.write("Hello World")
#
# #you can use for loop to accomplish this
# list = ["\n" + "Line1", "Line2", "Line3"]
#
# for item in list:
#     file.write(item + "\n")

#appending lines to text file
# file = open("example3.txt", 'a')
# file.write("Line 4")
# file.write("Line 4")
# file.write("Line 4")
# file.write("Line 4")
# file.write("Line 4")

# all other file handling modes

# r - opens file for reading only
#
# r+ opens file for both reading and writing
#
# w opens a file for writing only
#
# w+ opens file for reading and writing
#
# a opens for appending
#
# a+ opens for appending and reading

#use a with statement to automatically close file

with open("example3.txt", "a+") as file:
    file.seek(0)
    content=file.read()
    file.write("Line 6")
