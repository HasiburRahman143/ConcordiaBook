from django.urls import path
from .views import textbooks_by_course

urlpatterns = [
    path('<str:course_code>/', textbooks_by_course, name='textbooks_by_course'),
]
