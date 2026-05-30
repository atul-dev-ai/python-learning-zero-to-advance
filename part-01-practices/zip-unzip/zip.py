names = ['Atul', 'Ankit', 'Anik']
marks = [90, 80, 70]

for i in range(len(names)):
    print(names[i], marks[i]);

for name, mark in zip(names, marks):
    print(name, mark)