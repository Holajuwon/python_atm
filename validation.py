def acc_number_validation(acc_number):
    if acc_number:
        if len(str(acc_number)) == 10:
            try:
                acc_number = int(acc_number)
            except ValueError:
                print(
                    'Invalid Account Number, account number should be integer')
                return False
            finally:
                return acc_number
        else:
            print('Account Number cannot be more or less than 10 digits')
            return False
    else:
        print("Account Number is a required field")
        return False
