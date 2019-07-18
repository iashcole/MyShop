from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('', views.UserFormView.as_view(), name='register-page'),
]