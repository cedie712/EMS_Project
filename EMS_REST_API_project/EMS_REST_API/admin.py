from django.contrib import admin
from . models import Employee, EmployeeConfig, EmployeeProfile, AttendanceLog, SalaryReport, GlobalConfig

admin.site.site_header = 'EMS Project'

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeConfig)
admin.site.register(EmployeeProfile)
admin.site.register(AttendanceLog)
admin.site.register(SalaryReport)
admin.site.register(GlobalConfig)

