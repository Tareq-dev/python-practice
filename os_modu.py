import os
 
 

# Current working directory
# print(os.getcwd())

# # নতুন ফোল্ডার তৈরি
# os.mkdir("test_folder")

# সব ফাইল দেখাও
# print(os.listdir())

# ফোল্ডার ডিলিট (আগে খালি হতে হবে)
# os.rmdir("test_folder")

# Environment variable পাওয়া
# print(os.getenv("\python-practice\.env"))
 
from dotenv import load_dotenv

# তোমার .env ফাইলের অবস্থান
load_dotenv("D:\\python-practice\\.env")

# ✅ .env ফাইল থেকে ডেটা পড়ো
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
api_key = os.getenv("API_KEY")

# ✅ প্রিন্ট করে দেখি
print("Database Configurations:")
print(f"Host: {db_host}")
print(f"User: {db_user}")
print(f"Password: {db_pass}")
print()
print(f"API Key: {api_key}")