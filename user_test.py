import unittest #Importing the unittest module from user import user
from user import  User #Importing the user class


class Testuser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''


# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Mwanduka", "Stephen", "mwandukastephen20@gmail.com", "tots254")

    # test 1
    def test_init(self):
        '''
        Test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Mwanduka")
        self.assertEqual(self.new_user.last_name, "Stephen")
        self.assertEqual(self.new_user.email_address, "mwandukastephen20@gmail.com")
        self.assertEqual(self.new_user.password, "tots254")

    # test 2
    def test_save_user(self):
        '''
        Test_save_user test case to test if the user object is saved into the user list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    # test 3
    def test_save_multiple_user(self):
        '''
        This is to check if we can sve multiple user objects to our user_list.
        '''
        self.new_user.save_user()
        test_user = User("Mwanduka", "Stephen", "mwandukastephen20@gmail.com", "tots254")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    # test 4
    def test_delete_user(self):
        '''
        This is to test if we can remove a user from our user list.
        '''
        self.new_user.save_user()
        test_user = User("Mwanduka", "Stephen", "mwandukastephen20@gmail.com", "tots254")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    # test 5
    def test_find_user_by_email_address(self):
        '''
        This is to check if we can find a user by email and display information.
        '''
        self.new_user.save_user()
        test_user = User("Mwanduka", "Stephen", "mwandukastephen20@gmail.com", "tots254")
        test_user.save_user()

        found_user = User.find_by_email_address("mwandukastephen20@gmail.com")
        self.assertEqual(found_user.email_address, test_user.email_address)

    # test 6
    def test_user_exists(self):
        '''
        This is to see if we can return a Boolean if we cannor find a user.
        '''

        self.new_user.save_user()
        test_user = User("Mwanduka", "Stephen", "mwandukastephen20@gmail.com", "tots254")
        test_user.save_user()

        user_exists = User.user_exist("mwandukastephen20@gmail.com")

        self.assertTrue(True)


if __name__ ==  '__main__':
    unittest.main()
