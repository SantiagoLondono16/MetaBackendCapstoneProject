#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
]