
from utils.validator import Validation_Iban, check_user_inBase

def Register_user(user, List):
    
    if Validation_Iban(user[2]) and not check_user_inBase(user[2],List):
        List.append({'name': user[0], 'surname': user[1], 'acc_number': user[2], 'balance': 0})
        print(F'user correctly added {List}')
    else:
        print('Entered wrong account number or already exist')
        return Register_user([input('enter user name: '), input('enter user surname: '), input('enter user account number: ')], List)