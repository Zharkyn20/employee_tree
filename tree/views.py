from django.shortcuts import render

from tree.models import Employee, Department


def index(request):
    dep_queryset = Department.objects.all()
    empl_queryset = Employee.objects.all()

    return render(
        request,
        "index.html",
        context={"departments": dep_queryset, "employees": empl_queryset},
    )
