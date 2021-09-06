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

