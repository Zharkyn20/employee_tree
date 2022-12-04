from django.template import Library

from tree.models import Employee

register = Library()


@register.filter()
def in_department(department):
    return Employee.objects.filter(department=department)
