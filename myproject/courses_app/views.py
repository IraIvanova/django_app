from django.shortcuts import render, redirect
from django.views import View
from .utils import create_form
from .models import Course


class CourseFormPage(View):
    template_name = 'form.html'

    def get(self, request):
        is_auth_user = request.user.is_authenticated
        form = create_form()

        data = {
            'is_auth_user': is_auth_user,
            'form': form
        }

        return render(request, self.template_name, data)

    def post(self, request):
        form = create_form(request_data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            Course.objects.get_or_create(name=name)
            return redirect('courses_index')


class CoursesPage(View):
    template_name = 'courses_list.html'

    def get(self, request):
        form = create_form()
        courses = Course.objects.all()

        data = {
            'form': form,
            'courses': courses
        }

        return render(request, self.template_name, data)


class CoursePage(View):
    template_name = 'course_page.html'

    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)

        return render(request, self.template_name, {'course': course})
