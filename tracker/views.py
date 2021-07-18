from django.shortcuts import render, redirect
from .models import Expense
from .forms import expenseForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import User
from django.core.paginator import Paginator

@unauthenticated_user
def loginPage(request):
    login_form = CreateUserForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            messages.info(request, 'Username OR Password is Incorrect')
            


    context = {'login_form':login_form}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def registerPage(request):
    register_form = CreateUserForm()

    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, 'Account Created Successfully for' + user )
            return redirect("login")

    context = {'register_form':register_form}

    return render(request, 'register.html', context)

@login_required(login_url='login')  
#@allowed_users(allowed_roles=['admin'])
def main(request):
    expenses = Expense.objects.all()
    user = request.user
    Data = Expense.objects.filter(user=user)

    context = {'expenses': expenses, 'data': Data}

    return render(request, 'tracker/dashboard.html', context)

@unauthenticated_user
def userPage(request):
    context = {}
    return render(request, 'user.html', context)

@login_required(login_url='login') 
def createExpense(request):
    expense = expenseForm()

    if request.method == "POST":
        expense = expenseForm(request.POST)
        if expense.is_valid():
            Expense = expense.save(commit=False)
            Expense.user = request.user
            Expense.save()
            expense.save()
            return redirect("main")
            
    return render(request, 'tracker/create-expense.html', {'expense': expense})

@login_required(login_url='login') 
def updateExpense(request, pk):
    expense = Expense.objects.get(id=pk)
    form = expenseForm(instance=expense)
    
    if request.method == 'POST':
        form = expenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("main")
    context = {'form':form}
    return render(request, 'tracker/update-expense.html', context)

@login_required(login_url='login') 
def deleteExpense(request, pk):
    expense = Expense.objects.get(id=pk)

    if request.method == 'POST':
        expense.delete()
        return redirect("main")

    context = {'expense':expense}
    return render(request, 'tracker/delete-expense.html', context)

