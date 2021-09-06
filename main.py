from user import User
from social import Credentials


def create_user(acc_name, user_name, password, email):
    '''
    Function to create a new user
    '''
    new_user = User(acc_name, user_name, password, email)
    return new_user


    def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


    def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


    def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)


    def check_existing_user(name):
    '''
    Function that check if a user exists and return a Boolean
    '''
    return User.user_exist(name)


    def display_user():
    '''
    Function that returns saved users
    '''
    return User.display_users()


    def create_credentials( user_name, password, email):
    '''
    Function to create a new user
    '''
    new_credentials = Credentials(user_name, password, email)
    return new_credentials


    def save_credentials(credentials):
    '''
    Function to save user
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
    Function to delete a user
    '''
    credentials.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return Credentials.find_by_name(name)


def check_existing_credentials(name):
    '''
    Function that check if an user exists and return a Boolean
    '''
    return Credentials.credentials_exist(name)


def display_credentials():
    '''
    Function that returns saved users
    '''
    return Credentials.display_credentials()


    def main():
    print("WELCOME TO PASSWORD LOCKER.")
    print("What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to Password Locker to create an account.")
    print('\n')
    while True:
        print("You can use these short codes to navigate through :\n sn for Sign Up.\n da for display your account.\n lg for login.\n ex for exit. ")
        short_code = input().lower()
        if short_code == 'sn':
            print("Create an  Account")
            print("_"*100)
            acc_name = input('Account name:')
            print('\n')
            user_name = input('User name:')
            print('\n')
            pwd = input('Password : ')
            print('\n')
            e_address = input('Email address:')
            save_user(create_user(acc_name, user_name, pwd, e_address))
            print('\n')
            print(
                f"Congratulations {acc_name} an Account with the user name  {user_name} has been created successfully.")
            print(
                f"You can now login to your {acc_name} account using the password you created.")
            print('\n')


             elif short_code == 'da':
            if display_user():
                print("Thank you for signing up. Here are your login credentials")
                print('\n')
                for user in display_user():
                     print(
                         f"User name:{user.acc_name}  User name: {user.user_name} Password:{user.password}")
                     print('\n')
            else:
                print('\n')
                print(
                     "Invalid username or password.")
                print('\n')
                 elif short_code == 'lg':
            print("Enter your password to login.")
            search_user = input()
            if check_existing_user(search_user):
                find_credentials = find_user(find_user)
                print("\033[1;32;1m   \n")
                print(f"Hello.Welcome to {user_name} account")
                print("\033[1;37;1m   \n")




