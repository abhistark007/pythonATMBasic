print("Welcome to SAINTSCREED bank!")
pin=5678
chances=3
balance=50000
while chances!=0:
    user_pin=int(input("Enter your pin : "))
    if user_pin!=pin:
        chances=chances-1
        print("Wrong pin number ")
        print(f"You have {chances} chances left")
    else:
        user_choice=input("B: balance, D: deposit, W: withdraw")
        if user_choice=="B" or user_choice=="b":
            print(f"Your total balance is {balance}")
        if user_choice=="D" or user_choice=="d":
            deposit_user=int(input("Enterthe amout to be diposited : "))
            balance=balance+deposit_user
            print(f"You have deposited Rs{deposit_user}")
            print(f"Your total balance is Rs{balance}")

        if user_choice=="W" or user_choice=="w":
            withdraw_user=int(input("Enter the amout to be withdrawn : "))
            balance=balance-withdraw_user
            print(f"You have withdrawn Rs{withdraw_user}")
            print(f"Total balance remaining is {balance}")

    user_exit=input("Would you like to exit (Y/N)?")
    if user_exit=="Y" or user_choice=="y":
        print("Adios amigos")
        break
    else:
        continue
