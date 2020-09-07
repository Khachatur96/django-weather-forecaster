from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('farenheit_city',views.farenheit_city, name = 'farenheit_city'),
    path('search/', views.searched_city, name='searched_city'),
    path('yourcity/', views.your_city, name='your_city'),
    path('sevendays/', views.seven_days, name='seven_days'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('farenheit/', views.farenheit, name="farenheit"),
    path('sevendaysfarenheit/', views.seven_days_farenheit, name='seven_days_farenheit'),
    path('yourcityfarenheit', views.your_city_farenheit, name= 'your_city_farenheit' )
]
