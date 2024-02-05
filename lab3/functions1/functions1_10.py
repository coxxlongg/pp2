def unique(list):
    unList = []
    for i in list:
        if i not in unList:
            unList.append(i)
    return unList