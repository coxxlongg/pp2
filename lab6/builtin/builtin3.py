def palindrome(string):
    reverse = ''.join(reversed(string))

    if (string == reverse):
        return True
    return False