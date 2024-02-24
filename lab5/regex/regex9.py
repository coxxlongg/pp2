import re

def inserter(text):
    
    second = re.sub(r'(\B)([A-Z])', r'\1 \2', text)
    return second