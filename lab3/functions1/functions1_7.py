def has_33(list):
    for i in range (len(list) + 1):
        if list[i] == 3 and list[i+1] == 3:
            return True
    return False