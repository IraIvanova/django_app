from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(label="Course Name")
