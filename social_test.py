import unittest
from social import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials = Credentials( "Ephraim", "password3031", "ebundi04@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.user_name, "Ephraim")
        self.assertEqual(self.new_credentials.password, "password3031")
        self.assertEqual(self.new_credentials.email, "ebundi04@gmail.com")

        def test_save_credentials(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_credentials.save_credentials()  
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []
            def test_save_multiple_credentials(self):
        '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Ephraim", "password3031", "ebundi04@gmail.com")
        test_credentials.save_credentials()
           
  
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
            test_delete_account to test if we can remove an account from our account list
            '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Ephraim", "password3031", "ebundi04@gmail.com")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  
        self.assertEqual(len(Credentials.credentials_list), 1)

    

if __name__ == '__main__':
    unittest.main()

 