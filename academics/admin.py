from django.contrib import admin

from .models import Course, Department, Program


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "hod_name")
    search_fields = ("name", "hod_name")


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_years", "department")
    list_filter = ("department",)
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_code", "course_name", "credits", "semester", "program")
    list_filter = ("semester", "program")
    search_fields = ("course_code", "course_name")
