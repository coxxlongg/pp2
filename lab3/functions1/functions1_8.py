def spy_game(nums):
    seq = [0, 0, 7]
    index = 0
    for inum in nums:
        if inum == seq[index]:
            index += 1
            if index == len(seq):
                return True
    return False