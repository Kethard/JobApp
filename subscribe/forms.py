from django import forms
from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={
            'first_name':('Enter first name'),
            'last_name':('Enter Last Name'),
            'email':('Enter email')
        }
        error_messages ={
            'first_name':{
                'required':('You have to enter your name')
                },
            'last_name':{
                'required':('You have to enter your name')

            }
        }
       # fields = '__all__'  wyświetla wszystie pola z formularza
# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid Last Name')
#     return value
# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100,label="Enter Your Name", validators=[validate_comma])
#     last_name = forms.CharField(max_length=100,label="Last name", validators=[validate_comma])
#     email = forms.EmailField(max_length=100,label="Email",)