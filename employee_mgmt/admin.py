from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'role')
    list_filter = ('department', 'role')
    search_fields = ('name',)
    fieldsets = (
        # section 1:
        ('Personal Info', {
            'fields': ('name', 'department', 'role')
        }),
        # section 2:
        ('Contact', {
            'fields': ('email',)
        })
    )
