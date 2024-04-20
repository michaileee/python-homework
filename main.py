from moduls.register import Register_user
from moduls.refunder import Deposit_Money
from moduls.transferer import Transfer_Money 

#მომხმარებლების ანგარიშების ბაზა
List = [{"name": "Otar", "surname": "terterashvili", "acc_number": "TB001", "balance": 0},
    {"name": "jon", "surname": "doe", "acc_number": "TB003", "balance": 0},
    {"name": "Giorgi", "surname": "Sharikadze", "acc_number": "TB004", "balance": 0}]

#ძირითდი ოპერაციების გამოძახება
def main():      
    while True:
        Operation = input(''' ::::::Operations::::::: 
        1.Register_User
        2.Deposit_Money
        3.Transfer_Money
        4.Exit
        Choose Operation:: ''')
        if Operation == '1':
            user = [input('enter user name: '), input('enter user surname: '), input('enter user account number: ')]
            Register_user(user, List)
        elif Operation == '2':
            user_money = [input('enter account number: '), input('enter amount: ')]
            Deposit_Money(user_money, List)
        elif Operation == '3':
            riciver_user = input('enter reciver account number: ')
            sender_user = input('enter sender account number: ')
            amount = input('enter transaction amount: ')
            Transfer_Money(riciver_user, sender_user, amount, List)
        elif Operation == '4':
            break
        else:
            print('wrong command, choose number from Operation list')

if __name__ == "__main__":
    main()
