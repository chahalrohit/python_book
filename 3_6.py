# Program to authenticate user and allow access to system 

def authenticateUser(password):
    if password == 'magic':
        message = 'Login Successful \n Welcome to system'
    else:
        message = 'Password mismatch !!\n'
    return message


def main():
    print('\t LOGIN SYSTEM')
    print('===============')
    password = input('Enter password : ')
    message = authenticateUser(password)
    print(message)


if __name__ == '__main__':
    main()
