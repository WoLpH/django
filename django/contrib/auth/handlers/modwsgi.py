from django.contrib.auth.models import User
from django import db

def authenticate_user(environ, user, password):
    """
    Authentication handler that checks against Django's auth database
    """

    db.reset_queries() 

    kwargs = {'username': user, 'is_active': True} 

    try: 
        # verify the user exists
        try: 
            user = User.objects.get(**kwargs) 
        except User.DoesNotExist: 
            return None

        # verify the password for the given user
        if user.check_password(password): 
            return True
        else: 
            return False
    finally: 
        db.connection.close()

