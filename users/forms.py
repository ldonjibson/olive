from django import forms
from .models import UserProfile
# from smsangonumcredit.models import NumberCredits
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
User = get_user_model()
from django_countries.widgets import CountrySelectWidget


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
          'first_name',
          'last_name',
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
          'location',
          'status_word',
          'bio',
          'position',
          'address',
          'gender',
          'date_of_birth',
          'profile_photo',
          'phone',
          'country',
          'postal_code',
        ]
        widgets = {
            'date_of_birth':forms.DateInput(attrs={'type':'date'}),
            'profile_photo':forms.ClearableFileInput(attrs={'type': 'file'}),
            'phone':forms.NumberInput(attrs={'type': 'number', 'placeholder':'2348100001111', 'min':'2347000000000','max':'2349999999999'}),
            'country': CountrySelectWidget(),
            'postal_code': forms.NumberInput(attrs={'type': 'number', 'placeholder':'100001'}),
            'address': forms.TextInput(attrs={'maxlength':300, 'required':False, 'placeholder':'Address'}),
            'gender': forms.Select(choices=GENDER_CHOICES),
            'bio': forms.Textarea(attrs={'maxlength':500}),
            'status_word': forms.TextInput(attrs={'maxlength':50, 'required':False, 'placeholder':'Watch word'}),
            'location': forms.TextInput(attrs={'maxlength':50, 'required':False, 'placeholder':'Location'}),
            'position': forms.TextInput(attrs={'maxlength':50, 'required':False, 'placeholder':'Position'}),
        }


class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(max_length=30, required=True, help_text='Required. Unique username')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2' )

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        match = User.objects.filter(email=email)
        
        if match:
	        raise forms.ValidationError('This email address is already in use.')
        else:
        	return email   