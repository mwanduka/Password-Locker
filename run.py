from credential import credential
def create_credentials(fname,lname,email,password):
    '''
    Function to create a new credential
    '''
    new_credential =  credential(fname,lname,email,password)
    return new_credentials

def save_credentials(user):
    '''
    Function to save credential
    '''
    credential.save_credential()

def save_credentials_multiple(user):
    '''
    Function to save credential
    '''
    credential.save_credentials_multiple()


def del_credentials(user):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_credentials(email):
    '''
    Function that finds a credential by the number and returns the credential
    '''
    return credential.find_by_number(email)

def check_existing_credentials(email):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return credential.credentials_exist(email)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return credential.display_credentials()

def main():
    print("Hello Welcome to your credential list. What is your name?")
    user_name = input()

    print(f'Hello {user_account}. What would you like to do?')
    print('\n')
    while True:
            print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list")
            short_code = input().lower()

            if short_code == 'cc':
                print("New credential")
                print("-"*10)

                print("First name ....")
                f_name = input()

                print("Last name ....")
                l_name = input()

                print("Phone number ....")
                p_number = input()

                print("Email address ....")
                e_address = input()

                save_credentials(create_credential(f_name,l_name,p_number,e_address)) #create and save new credential.
                print('\n')
                print(f'New credential{f_name}{l_name}created')
                print('\n')

            elif short_code == 'dc':
                if display_credentials():
                    print("Here is a list of all your credentials")
                    print('\n')
                    for credential in display_credentials():
                        print(f"{credential.first_name}{credential.last_name} .....{credential.number}")
                        print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')
            elif short_code == 'fc':
                    print("Enter the number you want to search for")
                    search_number = input()
                    if check_existing_credentials(search_number):
                        search_credential = find_credential(search_number)
                        print(f"{search_credential.first_name}{search_credential.last_name}")
                        print('-' *20)
                        print(f"Phone number.......{search_credential.password}")
                        print(f"Email address.......{search_credential.email}")
                    else:
                        print("That credential does not exist")
            elif short_code == "ex":
                        print("Bye .......")
                        break
            else:
                print("I really didn't get that. Please use the short codes")

# from user import user
# def create_user(fname,lname,email,password):
#     '''
#     Function to create a new user
#     '''
#     new_user =  user(fname,lname,email,password)
#     return new_account
#
# def save_users(account):
#     '''
#     Function to save user
#     '''
#     user.save_account()
#
# def del_user(account):
#     '''
#     Function to delete a account
#     '''
#     user.delete_account()
#
# def find_user(password):
#     '''
#     Function that finds a user by the number and returns the user
#     '''
#     return user.find_by_number(password)
#
# def check_existing_users(password):
#     '''
#     Function that check if a user exists with that number and return a Boolean
#     '''
#     return user.user_exist(password)
#
# def display_users():
#     '''
#     Function that returns all the saved users
#     '''
#     return user.display_users()
#
# def main():
#     print("Hello Welcome to your account list. Which do you what to login?")
#     user_account = input()
#
#     print(f'Hello {user_name}. What would you like to do?')
#     print('\n')
#     while True:
#             print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list")
#             short_code = input().lower()
#
#             if short_code == 'cc':
#                 print("New user")
#                 print("-"*10)
#
#                 print("First name ....")
#                 f_name = input()
#
#                 print("Last name ....")
#                 l_name = input()
#
#                 print("Password ....")
#                 p_number = input()
#
#                 print("Email address ....")
#                 e_address = input()
#
#                 save_users(create_user(f_name,l_name,p_number,e_address)) #create and save new user.
#                 print('\n')
#                 print(f'New user{f_name}{l_name}created')
#                 print('\n')
#
#             elif short_code == 'dc':
#                 if display_users():
#                     print("Here is a list of all your accounts")
#                     print('\n')
#                     for user in display_users():
#                         print(f"{user.fname}{user.last_name} .....{user.number}")
#                         print('\n')
#                 else:
#                     print('\n')
#                     print("You dont seem to have any accounts saved yet")
#                     print('\n')
#             elif short_code == 'fc':
#                     print("Enter the password of the account you want to search for")
#                     search_number = input()
#                     if check_existing_users(search_password):
#                         search_user = find_user(search_password)
#                         print(f"{search_user.first_name}{search_user.last_name}")
#                         print('-' *20)
#                         print(f"Password.......{search_user.password}")
#                         print(f"Email address.......{search_user.email}")
#                     else:
#                         print("That account does not exist")
#             elif short_code == "ex":
#                         print("Bye .......")
#                         break
#             else:
#                 print("I really didn't get that. Please use the short codes")
#
# if __name__ == '__main__':
#
#     main()
