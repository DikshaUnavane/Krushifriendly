from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path('payments/', views.payment_history, name='payment_history'),
    path('step6/', views.home_after_login, name='home_after_login'),

]
