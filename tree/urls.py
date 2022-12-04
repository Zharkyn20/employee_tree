# blog.links
from django.urls import path

from tree.views import DepartmentListView, EmployeeByDepartmentView

# app_name = 'tree'
urlpatterns = [
    path('', DepartmentListView.as_view(), name='department-list'),
    path('<str:name>/', EmployeeByDepartmentView.as_view(), name='employee-by-department'),

]