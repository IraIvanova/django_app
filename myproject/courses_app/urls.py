from django.urls import path
from .views import CourseFormPage, CoursesPage, CoursePage

urlpatterns = [
    path('', CoursesPage.as_view(), name='courses_index'),
    path('form', CourseFormPage.as_view(), name='save_course'),
    path('show/<int:course_id>', CoursePage.as_view(), name='show_course'),
]
