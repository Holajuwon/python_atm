def login():
    import main_file
    from bank_operations import bank_operation
    from validation import acc_number_validation

    print('********* Login into your account ********** \n')

    acc_number_from_user = input('Enter your account number: \n')
    acc_number_from_user = acc_number_validation(acc_number_from_user)

    if acc_number_from_user:
        password = input('Enter your password: \n')

        for acc_number, details in main_file.database.items():
            if acc_number == acc_number_from_user:
                if password == details[3]:
                    return bank_operation(details)
            else:
                print('Invalid account number or password, Try Again.')
                login()
    else:
        main_file.init()


def logout():
    print('You have logged out of our system')
    userInput = int(
        input('Do you want to perform another operation 1 (yes) 2 (no) \n'))
    if userInput == 1:
        login()
    elif userInput == 2:
        exit()
    else:
        print('Invalid option, try again')
        logout()


def register():
    from main_file import database
    from account_generator import gen_account_number

    print('********* Register An Account With Us ********')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a secure password for your account: \n')
    acc_number = gen_account_number()
    details = [first_name, last_name, email, password, acc_number, 0]
    database[acc_number] = details
    print('============================')
    print('Your Account has been created')
    print('Here is your account number %s' % acc_number)
    print('Make sure you keep it safe !')
    print('============================')

    login()
