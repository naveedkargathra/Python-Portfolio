import random

def password_generator(no_pass, char_length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFgHIJKLMNOPQRSTUVWXYZ.:()!@#0123456789'
    for p in range(int(no_pass)):
        passwords = ''
        for c in range(int(char_length)):
            passwords += random.choice(chars)
        print(passwords)


print("PASSWORD GENERATOR")
no_pass = input('Enter the number of passwords to create:')
char_length = input('Enter the length of characters required:')
print("Here are your passwords:")
password_generator(int(no_pass), int(char_length))