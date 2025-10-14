menu_list ={
    "Pizza": 150,
    "Pasta":200,
    "Fuska": 120,
    "Doi-Fuska":150,
    "Tea":40,
    "Coffee":100
}
#Greet
print("")
print("Welcome to Ayshu's Kitchen")
print("")
print("***************")
print("Pizza: 150 TK\nPasta: 200 TK\nFuska: 120 TK\nDoi-Fuska: 150 TK\nTea: 40 TK\nCoffee: 100 TK")
print("***************")
print("")

order_total = 0

item_1 = input("What you want to order? = ")

if item_1 in menu_list:
    order_total += menu_list[item_1]
    print(f"Your order item {item_1} added")
else:
    print(f"Order you selected like {item_1} is not available")

another_order = input("Do you want more? (Yes/No): ")
if another_order == "Yes" or "yes":
    item_2 = input("Enter your second item = ")
    if item_2 in menu_list:
        order_total += menu_list[item_2]
        print(f"Your second order {item_2} has been added")
    else:
        print(f"Your order item: {item_2} is not available!")

    print(f"Your total amount of order is {order_total} Taka")

    if item_1 and item_2 not in menu_list:
        print("You have not selected any of our items from menu ")
