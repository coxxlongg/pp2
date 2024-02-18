from datetime import datetime

current_datetime = datetime.now()

without_microsec = current_datetime.replace(microsecond=0)
print (without_microsec)