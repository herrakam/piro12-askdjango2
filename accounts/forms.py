from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    #UserCreationForm에 내용을 오버라이딩해 추가하고싶다면 여기에 쓸것
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
    pass