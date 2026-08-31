def show_menu():
    print("=" * 30)
    print("        ATM MENU")
    print("=" * 30)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=" * 30)
    
    

def check_balance():
    print("Available Balance  : ",balance)
    
    
def deposit(amount):
    global balance
    balance +=amount
    print("Successfully Deposited Amount : ",amount)
    
def withdraw(amount):
    global balance
    if balance < amount:
          print("Insufficient Balance")
    else:
          balance -= amount
          print("Successfully Withdrawn")


balance=1000


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        amount = int(input("Enter Amount: "))
        deposit(amount)

    elif choice == "3":
        amount = int(input("Enter Amount: "))
        withdraw(amount)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
