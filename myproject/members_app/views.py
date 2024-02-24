from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .utils import create_member_form
from .models import Member
from .forms import EditMemberForm
from courses_app.models import Course
from myproject.utils import ErrorConstants
from django.core.exceptions import ValidationError


# Create your views here.
class UsersListPage(View):
    index_template_name = 'users_list.html'
    user_template_name = 'user.html'

    def get(self, request, id=None):
        if id:
            user = User.objects.get(pk=id)
            return render(request, self.user_template_name, {'user': user})

        users = User.objects.all()
        return render(request, self.index_template_name, {'users': users})


class EditUserPage(View):
    user_template_name = 'user.html'

    def get(self, request, id):
        user = User.objects.filter(id=id).first()

        if not user:
            return render(request, ErrorConstants.error_404_template, {})

        form = EditMemberForm(instance=user)
        data = {
            'edit': True,
            'user': user,
            'form': form
        }

        return render(request, self.user_template_name, data)

    def post(self, request, id):
        user = User.objects.filter(id=id).first()

        if not user:
            return render(request, ErrorConstants.error_404_template, {})

        try:
            user.full_clean()
            form = EditMemberForm(request.POST, instance=user)
            if form.is_valid():
                courses = Course.objects.filter(pk__in=form.cleaned_data['courses'])
                for course in courses:
                    print(course)
                    course.enrolled_users.add(user)

                form.save()

        except ValidationError as e:
            print(e)

        return redirect('users')
    