from django.shortcuts import render

from tree.models import Employee, Department


# class DepartmentListView(ListView):
#     model = Department
#     template_name = "department_list.html"
#
#
# class EmployeeByDepartmentView(ListView):
#     model = Employee
#     context_object_name = 'employees'
#     template_name = 'employee_list.html'
#
#     def get_queryset(self):
#         self.department = Department.objects.get(name=self.kwargs['name'])
#         queryset = Employee.objects.filter(department=self.department)
#         print(queryset)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = self.department
#         return context


def index(request):
    dep_queryset = Department.objects.all()
    empl_queryset = Employee.objects.all()

    return render(request, "index.html", context={'departments': dep_queryset,
                                                  'employees': empl_queryset})


