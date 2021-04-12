def bank_operation(user):
    from auth import logout

    print('Welcome %s %s' % (user[0], user[1]))
    selected_option = int(
        input(
            "What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit  \n"
        ))
    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdrawal_operation(user)
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        print('#### Thanks for using our service. ####')
        exit()
    else:
        print("**** Invalid option, try again. ***")
        bank_operation(user)


def withdrawal_operation(user):
    withdraw = int(input('How much do you want to withdraw? \n'))
    user[-1] = user[-1] - withdraw
    print('Thank you for using this service, your account balance is %s' %
          user[-1])
    another_operation(user)


def deposit_operation(user):
    deposit = int(input('How much do you want to deposit?  \n'))
    user[-1] = user[-1] + deposit
    print('Thank you for using this service, your account balance is %s' %
          user[-1])
    another_operation(user)


def another_operation(user):
    option = int(
        input('Do you want to perform another operation? 1 (yes) 2 (no)\n'))
    if option == 1:
        bank_operation(user)
    elif option == 2:
        print('Thank you for using our service')
        exit()
    else:
        print('Invalid option')
        another_operation(user)
