import unittest
from user import User


class TestAccount(unittest.TestCase):
    def setUp(self):

       self.new_user = User("Instagram","Ephraim","password3031","ebundi@gmail.com")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.acc_name, "Instagram")
        self.assertEqual(self.new_user.user_name, "Ephraim")
        self.assertEqual(self.new_user.password, "password3031")
        self.assertEqual(self.new_user.email, "ebundi@gmail.com")

    def test_save_user(self):
        '''
        test_save_user testing if the user is saved into the user list
        '''
        self.new_user.save_user()  
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
            tear Down cleans up after each method has run
        '''
        User.user_list = []

    def test_save_multiple_users(self):
        '''
        test_save is basically to check if we can save multiple users into our user list
        '''
        self.new_user.save_user()
        test_user = User("Instagram", "Ephraim", "pasword3031", "ebundi04@gmail.com") 
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        
    def test_delete_user(self):
        '''
        test_delete is testing if we can delete our user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Instagram", "Ephraim", "paswor3031", "ebundi04@gmail.com")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)
        
    def test_find_user_by_user_name(self):
        '''
        test find user by name, checking if we can  find user by name and display info
        '''
        self.new_user.save_user()
        test_user = User("Instagram", "Ephraim", "pasword3031", "ebundi@gmail.com")
        test_user.save_user()
        get_user = User.find_by_name("Instagram")
        self.assertEqual(get_user.email,test_user.email)


    def test_user_exists(self):
        '''
        testing if user exists and if it can return a boolean if not found
        '''
        self.new_user.save_user()
        test_user = User("Instagram", "Ephraim", "pasword123", "ebundi04@gmail.com")
        test_user.save_user()
        user_exists = User.user_exist("pasword3031")
        self.assertTrue(user_exists)

    def test_display_users(self):
        '''
        this method returns all the users saved
        '''
        displayed = User.display_users()
        self.assertEqual(displayed,User.user_list)
       

if __name__ == '__main__':
    unittest.main()
