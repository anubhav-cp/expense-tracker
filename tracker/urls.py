from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('dashboard/', views.main, name='main'),
    path('login/', views.loginPage, name='login'),
    path('user/', views.userPage, name='user-page'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('create-expense/', views.createExpense, name='create-expense'),
    path('update-expense/<str:pk>/', views.updateExpense, name='update-expense'),
    path('delete-expense/<str:pk>/', views.deleteExpense, name='delete-expense'),
]
