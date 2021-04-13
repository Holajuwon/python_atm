class Budget:
    database = {}

    def __init__(self, category):
        self.database[category] = 0

    def deposit(self, category, amount):
        self.database[category] += amount
        return self.database[category]

    def withdraw(self, category, amount):
        if self.database[category] >= amount:
            self.database[category] -= amount
            return self.database[category]
        else:
            return f'Your available balance for category {category} is lower than the amount you desire to withdraw'

    def check_balance(self, category):
        return (f"Your balance is {self.database[category]}")

    def get_all_balance(self):
        return self.database

    def transfer(self, budget_from, budget_to, amount):
        if self.database[budget_from] >= amount:
            self.database[budget_from] -= amount
            self.database[budget_to] += amount
            return self.database
        else:
            return f'Your available balance for category {budget_from} is lower than the amount you desire to transfer'


def init():
    print('Welcome to your personal budgetting app')

    budget_name = input(
        'What is the name of the budget you want to create? \n')
    all_budgets = Budget(budget_name)

    def another_operation():
        try:
            option = int(
                input(
                    'What will you like to do next? \n 1. (Create another budget category?) \n 2. (Deposit Into your available budgets?) \n 3. (Withdraw from your existing budgets?) \n 4. (Get balance of a budget category?)  \n 5. (Get balance of all budgets?) \n 6. (Transfer funds between existing budgets?) \n 7. (Exit the app?) \n'
                ))
            return option
        except ValueError:
            print(
                '\n ********* Invalid option, only numbers 1-7 are valid options ******** \n'
            )
            another_operation()

    inOperation = True

    while inOperation:
        option = another_operation()

        if option == 1:
            budget_name = input(
                'What is the name of the budget you want to create? \n')
            Budget(budget_name)
        elif option == 2:
            category = input('What category do you want to deposit into? \n')
            amt = int(input('How much do you want to deposit? \n'))
            value = all_budgets.deposit(category=category, amount=amt)
            print(value)
        elif option == 3:
            category = input('What category do you want to withdraw from? \n')
            amt = int(input('How much do you want to deposit? \n'))
            value = all_budgets.withdraw(category=category, amount=amt)
            print(value)
        elif option == 4:
            category = input(
                'What category do you want to check its balance? \n')
            value = all_budgets.check_balance(category=category)
            print(value)
        elif option == 5:
            print(all_budgets.get_all_balance())
        elif option == 6:
            category_from = input(
                'What category do you want to transfer from? \n')
            category_to = input('What category do you want to transfer to? \n')
            amt = int(input('How much do you want to transfer? \n'))
            value = all_budgets.transfer(category_from, category_to, amt)
            print(value)
        elif option == 7:
            inOperation = False
            print("Thanks for using your personal budgetting app.")
            exit()
        else:
            print('Invlaid option')


init()