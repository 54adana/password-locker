import unittest # Importing the unittest module
from  credentials import User,Credentials # Importing the credentials class
import pyperclip

class TestUser(unittest.TestCase):

    


    def setUp(self):
        self.new_user =User ("Yvette","Adana","0786574531","yvetteadan2000@gmail.com") #Create password object
    
    def test_init(self):
        self.assertEqual(self.new_user.first_name,"Yvette")
        self.assertEqual(self.new_user.last_name,"Adana")
        self.assertEqual(self.new_user.phone_number,"0786574531")
        self.assertEqual(self.new_user.email,"yvetteadan2000@gmail.com")

        
       

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
         # saving the new user
        self.assertEqual(len(User.user_list),1)

        # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user =("Yvette","Adana","0786574531","yvetteadan2000@gmail.com") # user
            # test_user.save_user()



class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials =Credentials ("facebook","gift254","Yvette Adana")

    def test_init(self):
        self.assertEqual(self.new_credentials.account,"facebook")
        self.assertEqual(self.new_credentials.password,"gift254")
        self.assertEqual(self.new_credentials.user_name,"Yvette Adana")



    def test_save_credentials(self):
        self.new_credentials.save_credentials()
         # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

# setup and class creation up here
    def tearDown(self):
            Credentials.credentials_list = []

# other test cases here
    def test_save_multiple_credentials(self):
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook","gift254","Yvette Adana") # new credentials
        
# More tests above
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("facebook","gift254","Yvette Adana") # new credentials
            test_credentials.save_credentials()

    
    def test_find_credentials_by_password(self):
        '''
        test to check if we can find a credentials by phone number and display information
      '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook","gift254","Yvette Adana") # new credentials
        test_credentials.save_credentials()

        # found_credentials = Credentials.find_by_password("gift254")

        # self.assertEqual(found_credentials.credentials,test_credentials.password)
    
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook","gift254","Yvette Adana") # new contact
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("gift254")

        self.assertTrue(credentials_exists)
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
         

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found credential
    #     '''

    #     self.new_credentials.save_credentials()
    #     Credentials.copy_email("reneedaughty@gmail.com")

        # self.assertEqual(self.new_credentials.email,pyperclip.paste())
    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ ==  '__main__':
    unittest.main() # self.assertEqual(len(Credentials.credentials_list))