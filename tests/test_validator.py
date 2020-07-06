import unittest
from userValidator.classes.validator import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_it_will_reject_username_it_too_long(self):
        #Assume
        username = "usernameIsTooLong"
        #Action
        result = self.validator.username_is_valid(username)
        #Assert
        self.assertFalse(result)
    
    def test_it_will_reject_username_it_has_space(self):
        #Assume
        username = "Chan ga"
        #Action
        result = self.validator.username_is_valid(username)
        #Assert
        self.assertFalse(result)

    def test_if_will_reject_username_is_no_uppercase_character(self):
        #Assume
        username = "changa"
        #Action
        result = self.validator.username_is_valid(username)
        #Assert
        self.assertFalse(result)
    
    def test_it_will_accept_username_is_correct(self):
        #Assume
        username = "Changa"
        #Action
        result = self.validator.username_is_valid(username)
        #Assert 
        self.assertTrue(result)