from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from students.models import Student
from academics.models import Course
from .models import Attendance
from datetime import date

@login_required
def mark_attendance(request):
    if request.user.role != 'faculty':
        return redirect('login')

    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)

        for student in students:
            status = request.POST.get(str(student.id))
            Attendance.objects.create(
                student=student,
                course=course,
                date=date.today(),
                status=status
            )

        return redirect('faculty_dashboard')

    return render(request, 'attendance/mark_attendance.html', {
        'students': students,
        'courses': courses
    })