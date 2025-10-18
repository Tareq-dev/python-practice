from datetime import datetime, timedelta, date

# বর্তমান সময়
now = datetime.now()
# print("Now:", now)
# শুধু তারিখ
print("Today:", date.today())

# Custom format
print(now.strftime("%d-%m-%Y"))

# আগের বা পরের তারিখ
yesterday = date.today() + timedelta(days=1)
print("Yesterday:", yesterday)