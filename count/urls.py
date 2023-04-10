
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
]


urlpatterns = [
    path('',views.login, name='login'),
]

