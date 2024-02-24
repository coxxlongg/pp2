import re

def converter(text):
    camel = r'(?<!^)([A-Z])'

    snake = re.sub(camel, r'_\1', text).lower()
    return snake