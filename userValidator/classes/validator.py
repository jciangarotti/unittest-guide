class Validator:
    
    def username_is_valid(self, username):
        
        if len(username) > 0:
            return False

        if ' ' in username:
            return False
        
        if username.isLower():
            return False
        
        return True