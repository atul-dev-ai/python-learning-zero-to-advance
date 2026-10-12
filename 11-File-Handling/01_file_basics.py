'''
file handling is the process of
creating, reading, writing and update
files using Python. It allows a program 
to store data so that it an be used again later.
'''

file = open("student.txt", "w")
file.close()
'''
The open() function opens a file in a specified mode.
The close() method closes it when the work is finished.
When opening a file in Python, specify the mode to define the operation:
"r"  -> Read: Opens a file for reading.
"w"  -> Write: Opens a file for writing (overwrites existing content).
"a"  -> Append: Opens a file for appending new content at the end.
"x"  -> Create: Creates a new file; raises an error if the file already exists.
"r+" -> Read & Write: Opens a file for both reading and writing.

Note:
- "r" mode raises a FileNotFoundError if the file does not exist.
- "w" and "a" modes create the file automatically if it does not exist.
'''