'''
The "x" mode creates a new file exclusively.
If the file already exists, Python raises a FileExistsError.
'''
with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/new_exists.txt", "x") as file:
    file.write("name: Atul Paul\n")
print("File added successfully.")
# first time run korle file create korbe, ekoi code abar run korle file age thekei thakay error dibe.

'''
The "r+" mode always allows both reading and writng
in an existing file. It does not trucate the file automatically,
but writing can overwrite existing characters at the current position.
'''
