import re

text = "My email is tareq@example.com and phone 01712345678"

email = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(email)

phone = re.findall(r"01[0-9]{9}", text)
print(phone)

new_text = re.sub(r"\d", "*", text)
print(new_text)