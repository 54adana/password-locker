import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):


    def setUp(self):
        
        self.new_credentials = Credentials("Yvette","Adana","yvette754","yvetteadan2000@gmail.com") # create password object


    def test_init(self):
        self.assertEqual(self.new_credentials.first_name,"Yvette")
        self.assertEqual(self.new_credentials.last_name,"Adana")
        self.assertEqual(self.new_credentials.password,"yvette754")
        self.assertEqual(self.new_credentials.email,"yvetteadan2000@gmail.com")



    def test_save_credentials(self):
        self.new_credentials.save_credentials()
         # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),0)

# setup and class creation up here
    def tearDown(self):
            Credentials.credentials_list = []

# other test cases here
    def test_save_multiple_credentials(self):
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Renee","Daughty","ren221","reneedaughty@gmail.com") # new credentials
        
# More tests above
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("first_name","last_name","password","first_name@last_name.com") # new credentials
            test_credentials.save_credentials()

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved contact from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

        def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email,test_contact.email)        

if __name__ ==  '__main__':
    unittest.main() # self.assertEqual(len(Credentials.credentials_list),)