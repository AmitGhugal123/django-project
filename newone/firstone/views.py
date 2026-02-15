from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Student

# list page → show all students
def all_firstone(request):
    students = Student.objects.all()
    return render(request, 'firstone/all_firstone.html', {'students': students})

# detail page → single student
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'firstone/student_detail.html', {'student': student})