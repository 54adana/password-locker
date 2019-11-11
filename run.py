#!/usr/bin/env python3.6
from credentials import credentials
def create_credentials(fname,lname,password,email):
    '''
    Function to create a new credentials
    '''
    new_credentials = credentials(fname,lname,password,email)
    return new_credentials
def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    contact.save_credentials()
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    contact.delete_credentials()

def find_credentials(credentials):
    '''
    Function that finds a credentiuals by email and returns the password
    '''
    return Contact.find_by_credentials(credentials)

def check_existing_email(password):
    '''
    Function that check if a email exists with that password and return a Boolean
    '''
    return Credentials.credentials_exist(password)
    def main():
    print("Hello Welcome to your credentials list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credentials")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Password ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_credentials(create_credentials(f_name,l_name,password,e_address)) # create and save new credentials.
                            print ('\n')
                            print(f"New password {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your passwords")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{credentials.first_name} {credentials.last_name} .....{credentials.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the password you want to search for")

                            search_password = input()
                            if check_existing_credentials(search_number):
                                    search_credentials = find_password(search_password)
                                    print(f"{search_credentials.first_name} {search_credentials.last_name}")
                                    print('-' * 20)

                                    print(f"Password.......{search_credentials.password}")
                                    print(f"Email address.......{search_credentials.email}")
                            else:
                                    print("That password does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
main()