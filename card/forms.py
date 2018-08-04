from django import forms
from .models import carddetails
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class carddetailsForm(forms.Form):
	file = forms.FileField()
	title = forms.CharField(max_length= 100, 
		widget=forms.TextInput(
			attrs ={'placeholder' : 'Enter Title' }))
	description = forms.CharField(max_length= 500,
		widget=forms.TextInput(
			attrs ={'class': 'form-desc', 'placeholder' : 'Enter Description' }))


class addcommentForm(forms.Form):
	title = forms.CharField(max_length= 100, 
		widget=forms.TextInput(
			attrs ={'placeholder' : 'Your Comment' }))
    

