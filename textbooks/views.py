from django.shortcuts import render
from .models import Textbook

def textbooks_by_course(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)
    return render(request, 'textbooks/textbooks_list.html', {'textbooks': textbooks, 'course_code': course_code})
