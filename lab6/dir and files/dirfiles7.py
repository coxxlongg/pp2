def copy(source, destinatioin):

    with open(source, "r") as src:
        with open(destinatioin, "w") as dest:
            for line in src:
                dest.write(line)
