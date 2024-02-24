import re

def match_ab_pattern(text):
    pattern = r'ab{2,3}'
    
    if re.search(pattern, text):
        return True
    else:
        return False

