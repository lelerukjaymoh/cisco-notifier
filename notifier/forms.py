from django import forms
from notifier.models import login_credentials

class loginForm(forms.ModelForm):

    class Meta:
        model = login_credentials
        fields = ('email', 'password', 'phone',)

