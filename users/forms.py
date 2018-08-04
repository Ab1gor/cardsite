from django import forms
from .models import userdetails
from django.contrib.auth.models import User



class userdetailsForm(forms.Form):
	about = forms.CharField(max_length= 100, 
		widget=forms.TextInput(
			attrs ={'placeholder' : ''}))
	url = forms.CharField(max_length= 100, 
		widget=forms.TextInput(
			attrs ={'placeholder' : '' }))
	company = forms.CharField(max_length= 100, 
		widget=forms.TextInput(
			attrs ={'placeholder' : '' }))

