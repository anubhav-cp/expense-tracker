from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Expense

class expenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["amount", "date", "description", "category", "total_balance"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]