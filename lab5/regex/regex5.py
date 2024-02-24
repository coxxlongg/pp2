import re

def case(text):
    pattern = r'a.*b$'

    if re.search(pattern, text):
        return True
    else:
        return False