from menu import showmenu
from order_coffee import order_coffee
from history import showhistory

def main():
    
    while True:
        #show menu
        showmenu()
        option = input("enter an option: ")

        if option == "1":
            order_coffee()
        elif option == "2":
            showhistory()
        elif option == "3":
            print("Thank you for using our service!")
            break
        else:
            print("Invalid option")

#to call the function
if __name__ == "__main__":
    main()
