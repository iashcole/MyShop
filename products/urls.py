from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('register/', views.UserForm.as_view, name='register'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.ProductCreate.as_view(), name='product-add'),
]