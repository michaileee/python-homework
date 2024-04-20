
from utils.validator import Validation_Iban, check_user_inBase

#თანხის შეტანა ანგარიშზე
def Deposit_Money(user_money, List):
    
    if Validation_Iban(user_money[0]) and check_user_inBase(user_money[0], List) and user_money[1].isdecimal():
        check_user_inBase(user_money[0], List)['balance'] += int(user_money[1])
        print(f'user {user_money[0]} balance added {user_money[1]} Lari')
        print(List)
    else:
        print('not correct information, try again')
        return Deposit_Money([input('enter account number: '), input('enter amount: ')], List)    
    