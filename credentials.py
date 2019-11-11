import pyperclip
class Credentials:


     

    credential_list = []# Empty password list
     # Init method up here
    def save_credentials(self):
        pass
 
    def __init__(self,first_name,last_name,password,email):

        # docstring removed for simplicity

            self.first_name = first_name
            self.last_name = last_name
            self.password= password
            self.email = email

            # save_password method saves password objects into password_list
    def save_credentials(self):
        Credentials.credential_list.append(self)
        

    @classmethod
    def find_by_credentials(cls,password):
        '''
        Method that takes in a password and returns a credential that matches that password.

        Args:
            password: password to search for
        Returns :
            Credentials of person that matches the password.
        '''

        for password in cls.credentials_list:
            if credentials.password == password:
                return password

    @classmethod
    def copy_email(cls,email):
        credentials_found = Credentials.find_by_email(email)
        pyperclip.copy(credentials_found.email)