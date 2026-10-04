ORDERS = "coffee_machine/orders.txt"

def showhistory():

    print("\nOrder history:")

    try:
        #read the file and print the content
        with open(ORDERS, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("No orders yet")