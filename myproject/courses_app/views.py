from django.shortcuts import render, redirect
from django.views import View
from .utils import create_form
from .models import Course


class CoursesPage(View):
    index_template_name = 'courses_list.html'
    show_template_name = 'course_page.html'

    def get(self, request, course_id=None):
        form = create_form()
        if course_id:
            course = Course.objects.get(pk=course_id)
            return render(request, self.show_template_name, {'course': course})

        courses = Course.objects.all()
        data = {
            'form': form,
            'courses': courses
        }

        return render(request, self.index_template_name, data)

    def post(self, request):
        form = create_form(request_data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            Course.objects.get_or_create(name=name)
            return redirect('courses')
