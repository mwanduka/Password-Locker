class User:
    """
    Class that generates new instances of users
    """
    user_list = [] # Empty user list

    def __init__(self, first_name, last_name, email_address, password):

          # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password

    def save_user(self):
        '''
        This method saves user objects into the user_list.
        '''

        User.user_list.append(self)


    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


    @classmethod
    def find_by_email_address(cls, email_address):
        '''
        This method takes an email and returns user data that matches the email.
        Args:
            email: email address to search
        Returns:
            user information
        '''

        for user in cls.user_list:
            if user.email_address == email_address:
                return user

    @classmethod
    def display_users(cls,email_address):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def user_exist(cls,email_address):
        '''
        Method that checks if a user exists from the user listself.
        Args:
            password: email to search if it exists
        Returns:
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.password == email_address:
                return True

                return False
