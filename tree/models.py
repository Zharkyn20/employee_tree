from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    name = models.CharField(
        max_length=250,
        verbose_name="Название отдела"
    )
    parent = TreeForeignKey(
        "self",
        verbose_name="отдел-родитель",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="children",
    )

    def get_absolute_url(self):
        return reverse('employee-by-department', args=[str(self.name)])

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Employee(models.Model):
    department = TreeForeignKey(
        Department,
        verbose_name="отдел",
        on_delete=models.PROTECT,
        related_name="employees"
    )
    full_name = models.CharField(max_length=350)
    position = models.CharField(max_length=250)
    employment_date = models.DateField()
    salary = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.full_name}-{self.position}"
