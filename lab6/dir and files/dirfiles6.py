import os

directory = "./"

for i in range (65,91):
    filename = chr(i) + '.txt'
    filepath = os.path.join(directory, filename)
    with open (filepath, 'w') as file:
        file.write(chr(i))