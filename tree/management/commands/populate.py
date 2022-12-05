import random
from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from tree.models import Department, Employee
from populate_data import (
    DEPARTMENTS,
    ROOT_DEPARTMENTS,
    FIRST_NAMES,
    LAST_NAMES,
    POSITIONS
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_superuser()
        self.create_departments()
        self.create_employees()

    def create_departments(self):
        for root in ROOT_DEPARTMENTS:
            Department.objects.create(name=root)

        level = 0
        sub_departments_name = random.sample(DEPARTMENTS, k=10)
        while level < 4:
            parent_departments = Department.objects.filter(level=level)
            for name in sub_departments_name:
                parent = random.choice(parent_departments)
                Department.objects.create(
                    name=name,
                    parent=parent,)

            level += 1

    def create_employees(self):
        leaf_departments = Department.objects.filter(children__isnull=True)

        employee_objects = []
        for leaf in leaf_departments:
            for _ in range(5000):
                full_name = f'{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}'
                position = random.choice(POSITIONS)
                employment_date = date.today()
                salary = random.randint(500, 10000)

                employee_objects.append(Employee(
                    department=leaf,
                    full_name=full_name,
                    position=position,
                    employment_date=employment_date,
                    salary=salary
                ))
        Employee.objects.bulk_create(employee_objects)

    def create_superuser(self):
        User.objects.create_superuser(
            username='admin',
            password='admin',
        )

