from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import MPTTModel
from treewidget.fields import TreeForeignKey


class Department(MPTTModel):
    name = models.CharField(
        max_length=250,
        verbose_name="Название отдела"
    )
    parent = TreeForeignKey(
        "self",
        verbose_name="отдел-родитель",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
    )

    def __str__(self):
        return self.name

    def clean(self):
        parent_level = self.parent.get_level()
        if parent_level == 4:
            raise ValidationError("Иерархия отделов дозволена только до 5")


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

    def clean(self):
        if not self.department.is_leaf_node():
            raise ValidationError("Отдел должен быть листом (не иметь под отделов)")
        super(Employee, self).clean()
