
#ანგარიშის ნომრის არსებობის შემოწმება
def check_user_inBase(acc_number, List):
    for user in List:
        if user.get('acc_number') == acc_number:
            return user
    return None

#ვალიდაცია ანგარიშის ნომრის    
def Validation_Iban(acc_number):
    if len(acc_number)==5 and acc_number[0:2] =='TB' and acc_number[2:5].isdigit():
        return acc_number
    else:
        return None
