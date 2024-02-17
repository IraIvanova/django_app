from django.shortcuts import render, redirect
from django.views import View


class CoursesPage(View):
    template_name = 'index.html'

    def get(self, request):
        is_auth_user = request.user.is_authenticated

        return render(request, self.template_name, {'is_auth_user': is_auth_user})
