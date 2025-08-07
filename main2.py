#=====Cafe Management System========

menu = {
    'Cheezy Sandwich': 50,
    'Veggie Roll': 50,
    'Chicken Wrap': 75,
    'Pasta': 70,
    'Coffee': 80,
    'Tea': 100,
}

# Greet!
print("Welcome to the Cafe Management System")
print("Here is the menu:")
print("Cheezy Sandwich- $50\nVeggie Roll- $50\nChicken Wrap- $75\nPasta- $70\nCoffee- $80\nTea- $100")

Order_total = 0

#Take Order in a loop 
while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        Order_total += menu[item]
        print(f"{item} added to your order. Current total: ${Order_total}")
    else:
        print(f"Order item {item} is not available in the menu.")        
        another_order = input("Do you want to order another item?(yes/no):").lower()
        if another_order != "yes":
            break
        print(f"The total amount to pay is ${Order_total}. Thank You For Your Order!.")
          

