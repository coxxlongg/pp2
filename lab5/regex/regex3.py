import re

def case(text):
    pattern = r'[a-z]+_[a-z]+'
    
    if re.search(pattern, text):
        return True
    else:
        return False