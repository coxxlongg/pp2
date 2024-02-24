import re

def replace(text):
    pattern = r'[ ,.]'
        
    replaced = re.sub(pattern, ':', text)
    return replaced