from django import forms

class MemberForm(forms.Form):
    username = forms.CharField(label="Your Name")
    email = forms.EmailField(label="Your Email")