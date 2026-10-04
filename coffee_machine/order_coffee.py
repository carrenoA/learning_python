ORDERS = "coffee_machine/orders.txt"

def order_coffee():
    print("\nChoose a coffee:")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")

    choice = int(input("Enter your choice: "))

    coffee = {
        1: "espresso",
        2: "latte",
        3: "cappuccino"
    }

    if choice in coffee:
        #append in the file the option chosen
        with open(ORDERS, "a", encoding="utf-8") as file:
            file.write(f"{coffee[choice]}\n")
        print(f"You ordered a {coffee[choice]}")

    else:
        
        print("Invalid option")
        