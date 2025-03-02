from django.contrib import admin

from .models import Employee, Role, Department, AuditLog

admin.site.register(Employee)

admin.site.register(Role)

admin.site.register(Department)

admin.site.register(AuditLog)
# Register your models here.
