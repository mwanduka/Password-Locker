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

        def delete_user(self):
            '''
            delete_user method deletes a saved user from the user_list
            '''

            user.user_list.remove(self)


        @classmethod
        def find_by_password(cls,password):
            '''
            Method that takes in a email and returns a user that matches that password.

            Args:
                password: email to search for
            Returns :
                user of person that matches the password.
            '''

            for user in cls.user_list:
                if user.email == password:
                    return user

        @classmethod
        def display_users(cls,password):
            '''
            method that returns the user list
            '''
            return cls.user_list

        @classmethod
        def user_exist(cls,password):
            '''
            Method that checks if a user exists from the user listself.
            Args:
                password: email to search if it exists
            Returns:
                Boolean: True or false depending if the user exists
            '''
            for user in cls.user_list:
                if user.password == number:
                    return True

                    return False


        user_list = [] #Empty user user list
        #Init method up here
        def save_user(self):

            '''
            save_user method saves user objects into user-user_list
            '''

            user.user_list.append(self)
