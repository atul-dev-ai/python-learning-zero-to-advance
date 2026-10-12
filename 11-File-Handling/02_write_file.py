file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "w")
file.write("Name: Atul\n")
file.write("Department: CIS\n")
file.write("University: DIU\n")

file.close() # Output is saved to the text file, not shown in the terminal.

'''
The write() method writes text into a file.
The \n escape sequence movs the next text to a new line.
'''