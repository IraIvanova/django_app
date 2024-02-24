from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.views import View
from .utils import create_member_form
from .models import Member
from .forms import EditMemberForm
from courses_app.models import Course
from myproject.utils import ErrorConstants
from django.contrib.auth import get_user_model


# import pdb; pdb.set_trace()


# Create your views here.
class UsersListPage(View):
    index_template_name = 'users_list.html'
    user_template_name = 'user.html'

    def get(self, request, id=None):
        if id:
            user = get_user_model().objects.get(pk=id)
            return render(request, self.user_template_name, {'user': user})

        users = get_user_model().objects.all()
        return render(request, self.index_template_name, {'users': users})


class EditUserPage(View):
    user_template_name = 'user.html'

    def get(self, request, id):
        user = get_user_model().objects.filter(id=id).first()

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
        form = create_member_form(request_data=request.POST)

        return redirect('users')