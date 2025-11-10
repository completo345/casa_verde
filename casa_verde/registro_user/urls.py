from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('registro/',views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='registro_user/login.html'),name='login' ),
    path("logout/", LogoutView.as_view(), name="logout"),

]