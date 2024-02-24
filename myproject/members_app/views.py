from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .utils import create_member_form
from .models import Member
from .forms import EditMemberForm
from courses_app.models import Course
from myproject.utils import ErrorConstants


# import pdb; pdb.set_trace()


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

    def post(self, request):
        form = create_member_form(request_data=request.POST)

        # if form.is_valid():
            # name = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # Member.objects.get_or_create(name=name, email=email)

        return redirect('users')