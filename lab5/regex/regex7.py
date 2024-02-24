import re

def converter(text):
    snake = r'_([a-z])'

    camel = re.sub(snake, lambda match: match.group(1).upper(), text)
    return camel