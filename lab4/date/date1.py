from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

current_date_str = current_date.strftime("%Y-%m-%d")
new_date_str = new_date.strftime("%Y-%m-%d")

print(new_date_str)
