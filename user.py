class User:
    """
    Class that generates users new instances .
    """
    user_list = [] 

    def __init__(self,acc_name,user_name,password,email):
        self.acc_name = acc_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user(self):
        '''
        method that saves user into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        method that deletes user from user list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        for user in cls.user_list:
            if user.acc_name == name:
                return user


    @classmethod
    def user_exist(cls, name):
        '''
        method that checks if user exists
        Args:
            name: searching if user exists
        Returns :
            Boolean:returns true or false statement if the user exists or not
        '''
        for user in cls.user_list:
            if user.password == name:
                return user

        return False

    @classmethod
    def display_users(cls):
        """
        this method returns the account list
        """
        return cls.user_list