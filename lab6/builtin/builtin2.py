def lowup(string):
    upper = sum(1 for i in string if i.isupper())
    lower = sum(1 for i in string if i.islower())

    print(upper, lower)