import random
import string


def password():
    low_char = string.ascii_lowercase + string.ascii_uppercase

    # User Inputs
    nopassword = int(input("How many passwords? "))
    paslenght = int(input("Password Length?  "))

    # for the number of passwords required, execute the following the required amount of times:
        # for the required length of the password, take the password and add a random character chosen from the low characters.
        # print the password
    for pwd in range(nopassword):
        passwords = ""
        for c in range(paslenght):
            passwords += random.choice(low_char)
        print(passwords)


password()
