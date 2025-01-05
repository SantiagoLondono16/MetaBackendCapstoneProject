#define URL route for index() view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
    path('bookings/', include(router.urls)),
]