from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin

from tree.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee


class DepartmentAdmin(DraggableMPTTAdmin):

    # mptt_level_indent = 20
    expand_tree_by_default = True


admin.site.register(Department, DepartmentAdmin)
