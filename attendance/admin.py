from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "date", "status")
    list_filter = ("status", "date", "course")
    search_fields = (
        "student__full_name",
        "student__registration_number",
        "course__course_name",
        "course__course_code",
    )
