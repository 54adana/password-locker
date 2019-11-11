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