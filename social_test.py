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
