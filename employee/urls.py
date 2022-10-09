from django.urls import path
from employee import views

urlpatterns=[
    # path('index',views.index),
    # path('login',views.login),
    # path("signup",views.registration)
    path('login',views.LoginView.as_view()),
    path('signup',views.RegistrationView.as_view())
]

3