from userfeedback.models import *
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class userCommentsForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect())
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+254722222222'}))
    class Meta:
        required_css_class = 'required'
        model = userComments
        fields = ('phone_number','neighbourhood','comment','rating')