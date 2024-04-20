from utils.validator import Validation_Iban, check_user_inBase

def Transfer_Money(riciver_user, sender_user, amount, List):
    
    if Validation_Iban(riciver_user) and check_user_inBase(riciver_user, List):
        
        if Validation_Iban(sender_user) and check_user_inBase(sender_user, List):
            
            if amount.isdecimal():
                if check_user_inBase(sender_user, List)['balance'] >= int(amount):
                    check_user_inBase(riciver_user, List)['balance'] += int(amount)
                    check_user_inBase(sender_user, List)['balance'] -= int(amount)
                    print(f'you succesfuly transfer {amount} lari to {check_user_inBase(riciver_user, List)['name']} {check_user_inBase(riciver_user, List)['surname']}-s')
                else:
                    print('balance is not enough money')
                    return
            else:
                print('not correct amount number, try again')
                return Transfer_Money(riciver_user, sender_user, input('enter transaction amount: '), List)
        else:
            print('not valid sender account number, try again')
            return Transfer_Money(riciver_user, input('enter sender account number: '), amount, List)
    else:
        print('not valid riciver account number, try again')
        return Transfer_Money(input('enter reciver account number: '), sender_user, amount, List)