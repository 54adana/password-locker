import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):

    
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     # Items up here .......

    def setUp(self):
        
        Set up method to run before each test cases.
        
        self.new_contact = Contact("Yette","Adana","yvette754","yvetteadan2000@gmail.com") # create password object


    def test_init(self):
        
        test_init test case to test if the object is initialized properly
        

        self.assertEqual(self.new_credentials.first_name,"Yvette")
        self.assertEqual(self.new_credentials.last_name,"Adana")
        self.assertEqual(self.new_credentials.password,"yvette754")
        self.assertEqual(self.new_credentials.email,"yvetteadan2000@gmail.com")



def test_save_password(self):
        
        test_save_password test case to test if the password object is saved into
         the password list
    
        self.new_passworg.save_password() # saving the new password
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ ==  '__main__':
    unittest.main()