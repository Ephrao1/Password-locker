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




