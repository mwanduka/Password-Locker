import unittest #Importing the unittest module from user import user #Importing the user class
from user import  user


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
        user.user_list = []


# More tests above
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from a user user_list
        '''
        self.new_user.save_user()
        test_user = user("Test","user","0712345678","mwandukastephen20@gmail.com") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(user.user_list),1)

# other test cases here
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = user("Test","user","0712345678","mwandukastephen20@gmail.com") #new user
        test_user.save_user()
        self.assertEqual(len(user.user_list),2)

#Items up here ......

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = user("Test","user","0712345678","mwandukastephen20@gmail.com") # new user
        test_user.save_user()
        self.assertEqual(len(user.user_list),2)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        user.user_list.remove(self)

    def test_find_user_by_number(self):
        '''
        test to check if we can find a contract by phone number and display information
        '''
        self.new_user.save_user()
        test_user = user("Test","user","0711223344","mwandukastephen20@gmail.com") # new user
        test_user.save_user()

        found_user = user.find_by_number("0711223344")
        self.assertEqual(found_user.email,test_user.email)

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user listself.
        Args:
            number: Phone number to search if it exists
        Returns:
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.password == number:
                return True

                return False

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we can not find the user.
        '''

        self.new_user.save_user()
        test_user = user("Test","user","0711223344","test@test.com") # new user
        test_user.save_user()

        user_exists = user.user_exist("0711223344")
        self.assertTrue(user_exist)

    def test_display_all_users(self):
        '''
        method that returns all list of all user saved
        '''

        self.assertEqual(user.test_display_all_users(),user.user_list)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            user of person that matches the number.
        '''

        for user in cls.user_list:
            if user.password == number:
                return user

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("James", "Muriuki","0712345678","james@ms.com") #create user object
    # def test_init(self):
    #     '''
    #     test_init test case to test if the object is initialized properly
    #     '''
    #
    #     self.assertEqual(self.new_user.first_name,"James")
    #     self.assertEqual(self.new_user.last_name,"Muriuki")
    #     self.assertEqual(self.new_user.password,"0712345678")
    #     self.assertEqual(self.new_user.email,"james@ms.com")
    #
    #
    # def test_save_user(self):
    #     '''
    #     test_save_user test case to test if the user object is saved into
    #     the user list
    #     '''
    #     self.new_user.save_user() # saving the new user
    #     self.assertEqual(len(user.user_list),1)

if __name__ ==  '__main__':
    unittest.main()
