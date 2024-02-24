import re

def split(text):
    parts = re.split(r'(?=[A-Z])', text)
    
    parts = [part for part in parts if part]
    return parts