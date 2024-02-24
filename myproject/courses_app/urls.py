from django.urls import path
from .views import CoursesPage

urlpatterns = [
    path('', CoursesPage.as_view(), name='courses'),
    path('<int:course_id>', CoursesPage.as_view(), name='courses'),
    path('form', CoursesPage.as_view(), name='save_course'),
]
