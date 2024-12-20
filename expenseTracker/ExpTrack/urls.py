from django.urls import path
from . import views

urlpatterns = [
    path("",views.Login,name="login"),
    path("login",views.Login,name="login"),
    path("signup",views.signup,name="signup"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("logon1",views.logon1,name="logon1"),
    path("su",views.su,name="su"),
    path("logout",views.logout,name='logout'),
    path('api/income-expense/<str:emp_id>',views.income_expense_api,name='income_expense_api')
]