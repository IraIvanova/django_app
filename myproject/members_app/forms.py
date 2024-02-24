from django import forms
from courses_app.models import Course
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.models import User


class CreateMemberForm(UserCreationForm):
    field_order = ['username', 'email', 'password1', 'password2']
    email = forms.EmailField(label="Your Email")



    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        return user


class EditMemberForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    courses = forms.ModelChoiceField(
                        queryset=Course.objects.all().order_by('name'),
                        to_field_name='name',
                        label="Available courses"
                )