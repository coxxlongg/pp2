class stringEditor:
    def __init__(self):
        self.mystring = ""

    def getString(self):
        self.mystring = input()

    def printString(self):
        print(self.mystring.upper())

Myclass = stringEditor
Myclass.getString()
Myclass.printString()

