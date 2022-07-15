import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
today = today.strftime('%Y-%m-%d')
today_1 = today.replace('-0', '-', 1)
today_2 = today.replace('-0', '-')
today_3 = today_2[0:5] + '0' + today_2[5:]
yesterday = yesterday.strftime('%Y-%m-%d')
yesterday_1 = yesterday.replace('-0', '-', 1)
yesterday_2 = yesterday.replace('-0', '-')
yesterday_3 = yesterday_2[0:5] + '0' + yesterday_2[5:]

print(today, today_1, today_2, today_3, yesterday, yesterday_1, yesterday_2, yesterday_3)  # 不同格式的日期

