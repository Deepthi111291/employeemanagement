from django.urls import path
from calculator import views

urlpatterns=[
    path('home',views.HomeView.as_view(),name="calc-home"),
    path('add',views.AddView.as_view(),name="calc-add"),
    path('sub',views.SubView.as_view(),name="calc-sub"),
    path('mul',views.MulView.as_view(),name="calc-mul"),
    path('div',views.DivView.as_view(),name="calc-div"),
    path('wordcount',views.WordCountView.as_view(),name="calc-word"),
    path('prime',views.PrimeView.as_view(),name="calc-prime")
]
