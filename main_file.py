from random import randrange

database = {}


def init():
    import auth
    
    print('Welcome to crypto bank')
    have_account = int(
        input('Do you have an account With us? Enter: 1 (yes) 2(no) \n'))
    if (have_account == 1):
        auth.login()
    elif (have_account == 2):
        auth.register()
    else:
        print("You have selected an Invalid option")
        init()