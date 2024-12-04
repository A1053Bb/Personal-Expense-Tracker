from django.urls import path
from . import views

urlpatterns = [
    path("",views.Login,name="login"),
    path("login",views.Login,name="login"),
    path("signup",views.signup,name="signup"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logon1",views.logon1)
]