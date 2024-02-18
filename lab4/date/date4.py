from datetime import datetime

date1 = datetime(2024,3,15,13,0,0)
date2 = datetime(2024,3,16,13,0,0)

date_difference = date2 - date1
print(date_difference.total_seconds())
