import csv
from os.path import exists


class Savings:
    def __init__(self, account_name, user_name, balance=600):
        self.account_name = account_name
        self.balance = balance
        self.user_name = user_name

    def deposit(self, amount):
        """Deposit money into the account

        Args:
            amount (int): Amount being deposited into the account
        """

        # Save the current balance as the previous balance
        prev_balance = self.balance

        # Add add the amount to the current balance
        self.balance += amount
        print(f"You have deposited: ${amount}")
        print(f"New balance is: {self.balance}")

        # Recording transaction to file
        self.save_transaction(previous_balance=prev_balance, deposit=amount)
        print("Transaction has been saved")

    def withdraw(self, amount):
        """Withdraw money from the account
            Args:
                amount (int): Amount being withdrawn from the account
        """

        # Cannont withdraw if amount is greater than 65
        if amount > 65:
            print("You cannot withdraw more than $65")

        # Cannot withdraw if the remaining balance will be less than 45
        elif self.balance - amount < 45:
            print("Withdrawal failed as remaining balance will be less than $45")
        else:
            # save the current balance as the previous balance
            prev_balance = self.balance

            # subtract the withdraw amount
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}")
            print(f"You new account balance is ${self.balance}")

            # Recording transaction to file
            self.save_transaction(
                previous_balance=prev_balance, withdrawal=amount
            )
            print("Transaction has been saved")

    def calculate_interest(self, amount):
        """Calculates the interest on a given amount

        Args:
            amount (int): the amount if question
        """

        # calculate the interest
        interest = (6.56 / 100) * amount
        print(f"Interest on amount: {amount} is {interest}")

    def save_transaction(self, previous_balance, withdrawal=0, deposit=0):
        """Save the transaction to a csv file

        Args:
            previous_balance (int): the balance before the transaction
            withdrawal (int, optional): the amount being withdrawn. Defaults to 0.
            deposit (int, optional): the amount being deposited. Defaults to 0.
        """

        # check if file already exist
        if exists('bank.csv'):
            pass
        else:
            # if file does not exist, create a new file and add headings
            with open('bank.csv', mode='a') as bank_file:
                bank_writer = csv.writer(bank_file, delimiter=',')
                bank_writer.writerow(
                    [
                        'Account Name', 'User Name', 'Previous Balance', 'Withdrawal amount', 'Deposit Amount', 'New Balance'
                    ]
                )

        # save the transaction to the file
        with open('bank.csv', mode='a') as bank_file:
            bank_writer = csv.writer(bank_file, delimiter=',')
            bank_writer.writerow(
                [
                    self.account_name, self.user_name, previous_balance, withdrawal, deposit, self.balance
                ]
            )


# Instantiate clas
saving = Savings('Account 1', 'billy gilmour')

# Make a deposit
saving.deposit(50)
saving.deposit(120)

# Making a withdrawal
saving.withdraw(60)
saving.withdraw(50)


# Calculating interest
saving.calculate_interest(50)
