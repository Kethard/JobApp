from django import forms
def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError('Invalid Last Name')
    return value
class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=100,label="Enter Your Name", validators=[validate_comma])
    last_name = forms.CharField(max_length=100,label="Last name", validators=[validate_comma])
    email = forms.EmailField(max_length=100,label="Email",)