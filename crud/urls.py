from django.urls import path
from . import views

urlpatterns = [
  path('', views.login, name="login" ),
  path('login/', views.login, name="login" ),
  path('dashboard/', views.dashboard, name="dashboard"),
  path('clients/', views.clients, name="clients"),
  path('purchases/', views.purchases, name="purchases"),
  path('payments/', views.payments, name="payments"),
]