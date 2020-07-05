from userValidator.classes.validator import Validator

username = 'Changa'

validator = Validator()
if validator.username_is_valid(username):
    print("Username is Valid")

else:
    print("Username is invalid")