from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin

from tree.models import Employee, Department


class EmployeeInline(admin.StackedInline):
    model = Employee


class DepartmentAdmin(DraggableMPTTAdmin):
    inlines = [EmployeeInline]

    mptt_level_indent = 20
    expand_tree_by_default = True


admin.site.register(Department, DepartmentAdmin)
