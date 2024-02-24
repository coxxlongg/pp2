import re

def match_ab_pattern(text):
    pattern = 'ab*'
    
    if re.search(pattern, text):
        return True
    else:
        return False


