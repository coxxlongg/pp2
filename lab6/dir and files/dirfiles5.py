def writeList(file, list):

    with open(file, 'w') as f:
       for item in list:
           file.write(f"{item}\n")
