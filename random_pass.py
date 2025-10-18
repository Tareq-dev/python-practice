'''
Step-1 : number, lower, upper, symbol are taking in variable
Step-2 : make a random length(6 to 10 number)
Step-3 : Make a list of these 4 types of unique charecter 
Step-4 : add all charecter
Step-5 : while loop for extra charecter
Step-6 : append, shuffle and join then return
'''


import random

def generate_password():
    numbers = "0123456789"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"
                                
    length = random.randint(6, 10)
    password = [
        random.choice(numbers),
        random.choice(lower),
        random.choice(upper), 
        random.choice(symbols)
    ]
    all_chars = numbers + lower + upper + symbols
    while len(password) < length:
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return "".join(password)

print(generate_password())