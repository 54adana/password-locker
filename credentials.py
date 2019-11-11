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

    