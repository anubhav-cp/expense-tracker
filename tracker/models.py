from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    total_balance = models.FloatField(null=True, blank=True)
    category = models.ManyToManyField('Category')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=200)
    created=  models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
