from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# user app forms.py

# User register form class

class RegisterForm(UserCreationForm):
    """User register class"""

    class Meta:

        """User register class meta"""      

        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'password1', 'password2']
        help_texts = {
            'username': '',
            'last_name': '',
            'first_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
