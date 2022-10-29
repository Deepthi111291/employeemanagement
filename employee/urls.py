from django.urls import path
from employee import views

urlpatterns=[
    # path('index',views.index),
    # path('login',views.login),
    # path("signup",views.registration)
    # path('index',views.IndexView.as_view()),
    # path('login',views.LoginView.as_view()),
    # path('signup',views.RegistrationView.as_view()),
    # path('profile/add',views.EmployeeCreateView.as_view(),name="emp-add")
    path('add',views.EmployeeCreateView.as_view(),name="emp-add"),
    path('all',views.EmployeeListView.as_view(),name="emp-list"),
    path('details/<str:emp_id>',views.EmployeeDetailView.as_view(),name="emp-detail"),
    path('change/<str:e_id>',views.EmployeeEditView.as_view(),name='emp-edit'),
    path('remove/<str:e_id>',views.remove_employee,name='emp-remove')
]