import unittest #Importing the unittest module from credential import credential #Importing the credential class
from credential import  credential


class Testcredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''


# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        credential.credential_list = []


# More tests above
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from a credential credential_list
        '''
        self.new_credential.save_credential()
        test_credential = credential("Test","user","account","password") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(credential.credential_list),1)

# other test cases here
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = credential("Test","user","0712345678","mwandukastephen20@gmail.com") #new credential
        test_credential.save_credential()
        self.assertEqual(len(credential.credential_list),2)

#Items up here ......

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = credential("Test","user","0712345678","mwandukastephen20@gmail.com") # new credential
        test_credential.save_credential()
        self.assertEqual(len(credential.credential_list),2)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        credential.credential_list.remove(self)

    def test_find_credential_by_number(self):
        '''
        test to check if we can find a contract by phone number and display information
        '''
        self.new_credential.save_credential()
        test_credential = credential("Test","user","mwandukastephen20@gmail.com","totscaro") # new credential
        test_credential.save_credential()

        found_credential = credential.find_by_password("totscaro")
        self.assertEqual(found_credential.email,test_credential.email)

    @classmethod
    def credential_exist(cls,number):
        '''
        Method that checks if a credential exists from the credential listself.
        Args:
            number: Phone number to search if it exists
        Returns:
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.password == number:
                return True

                return False

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean if we can not find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = credential("Test","user","0711223344","test@test.com") # new credential
        test_credential.save_credential()

        credential_exists = credential.credential_exist("0711223344")
        self.assertTrue(credential_exist)

    def test_display_all_credentials(self):
        '''
        method that returns all list of all credential saved
        '''

        self.assertEqual(credential.test_display_all_credentials(),credential.credential_list)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a credential that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            credential of person that matches the number.
        '''

        for credential in cls.credential_list:
            if credential.password == number:
                return credential

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = credential("Mwanduka", "Stephen","facebook","mwandukastephen20@gmail.com") #create credential object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name,"Mwanduka")
        self.assertEqual(self.new_credential.last_name,"Stephen")
        self.assertEqual(self.new_credential.last_name,"Facebook")
        self.assertEqual(self.new_credential.email,"mwandukastephen20@gmail.com")


    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
        the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(credential.credential_list),1)

if __name__ ==  '__main__':
    unittest.main()
