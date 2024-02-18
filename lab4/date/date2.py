from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)

tomorrow = today + timedelta(days=1)

yesterday_str = yesterday.strftime("%Y-%m-%d")
today_str = today.strftime("%Y-%m-%d")
tomorrow_str = tomorrow.strftime("%Y-%m-%d")

print(yesterday_str, today_str, tomorrow_str, )
