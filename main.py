# Take in the customer name, and bank.
# Look up and Return their balance
# If the customer is from South Africa, apply the SA bank charges, otherwise the normal bank charges
# As the customer how much they want to deposit or withdraw.
# Execute the transaction and print their current balance.
from bank import NetBank, Capitec, SABank, Bank
from customerlist import SignUp
import time


def withdraw_request():
    answer = input('Would you like to withdraw or Deposit? ').lower()
    value = int(input('How much ?'))

    if answer == 'withdraw':
        Bank.withdraw(value)
    elif answer == 'deposit':
        Bank.deposit()


def bank_atm():
    customer_name = input('Please put in your name: ')
    customer_country = input('Please put in the country of your bank: ')

    if customer_country == 'South Africa':
        customer_bank = input('Please select your SA Bank: ')
        if customer_bank == 'Nedbank':
            transaction_fee = NetBank.transaction_cost
            print(f'Your Transaction fee will be R{transaction_fee}')

        elif customer_bank == 'Capitec':
            transaction_fee = Capitec.transaction_cost
            print(f'Your Transaction fee will be R{transaction_fee}')

        else:
            transaction_fee = SABank.transaction_cost
            print(f'Your Transaction fee will be R{transaction_fee}')
    else:
        transaction_fee = Bank.transaction_cost
        print(f'Your Transaction fee will be R{transaction_fee}')

    bank_with_us = False
    for i in range(0, len(SignUp.namelist)):
        if SignUp.namelist[i] == customer_name:
            print(f'Your balance is {SignUp.objectlist[i].balance}')
            return True
        else:
            pass

    if not bank_with_us:
        print('You do not bank with us.')
        sign_up_request = input('Would you like to sign up? (Y/N)')
        if sign_up_request == 'Y':
            new_customer_name = input('Please provide your name: ')
            new_customer_bank = input('Please select your bank: ')
            SignUp(new_customer_name, 0, new_customer_bank)
            print(SignUp.namelist)
            print(SignUp.balancelist)
            print(SignUp.banklist)
            print('Thank you for signing up. We will take you back to the main screen')
            time.sleep(0.8)
            bank_atm()
        else:
            print('You were not able to sign up, see you soon.')

    else:
        pass


if __name__ == '__main__':
    bank_atm()
