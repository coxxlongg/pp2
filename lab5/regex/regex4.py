import re

def case(text):
    pattern = r'[A-Z][a-z]+'

    if re.search(pattern, text):
        return True
    else:
        return False