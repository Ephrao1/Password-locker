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
