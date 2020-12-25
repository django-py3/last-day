from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class RegularUser(AbstractUser):
    """
    Определим поля
    """
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    postal_code = models.CharField(max_length=25, null=False, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    sex = models.BooleanField(null=True, blank=True)
    # PositiveIntegerFiled = > Unsigned Int
    # null True=> что мы допускаем NULL значение в таблицах - отпечаток в бд
    # blank True => мы допускаем не назначение этого атрибута на уровне модели - валидатор