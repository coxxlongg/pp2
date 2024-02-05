def solve(numheads, numlegs):
    for numrab in range (numheads):
        numchick = numheads - numrab
        if numchick * 2 + numrab * 4 == numlegs:
            return numchick, numrab
