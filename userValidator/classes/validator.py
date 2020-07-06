class Validator:
    
    def username_is_valid(self, username):
        if len(username) > 10:
            return False
        if ' ' in username:
            return False
        if username.islower():
            return False
        
        return True