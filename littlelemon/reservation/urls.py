#define URL route for index() view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router2 = DefaultRouter()
router.register(r'', views.BookingViewSet)
router2.register(r'', views.UserViewSet)

urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
    path('bookings/', include(router.urls)),
    path('users/', include(router2.urls)),
    path('api-token-auth/', obtain_auth_token),
]