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
Python e open() korar somoy mode diye bole dite hoy,
file er songge ki kaj korbe.
"r" -> file theke read kora.
"w" -> file e lekha; porono content muche jete pare.
"a" -> file er seshe notun content soj kora(Append).
"x" -> notun file create kora; file age thakle error.
"r+" pora o lekha.

note: "r" mode e file na thakle error hoy.
      "w" and "a" mode e file na thakle normally create hoy.
'''