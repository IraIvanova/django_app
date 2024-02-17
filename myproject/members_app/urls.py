from django.urls import path
from .views import MemberPage

urlpatterns = [
    path('', MemberPage.as_view(), name='member_input'),
]
