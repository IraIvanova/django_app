from django.urls import path
from .views import CoursesPage

urlpatterns = [
    path('', CoursesPage.as_view(), name='courses_index'),
]
