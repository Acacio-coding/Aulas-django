from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard, name="dashboard"),
  path('clients/', views.clients, name="clients"),
  path('clients/details/<int:pk>', views.detalhes_cliente, name="detalhes_cliente"),
  path('clients/new/', views.clients_new, name="clients_new"),
  path('clients/<int:pk>/', views.clients_edit, name='clients_edit'),
  path('clients/remove/<int:pk>', views.clients_remove, name="clients_remove"),
  path('purchases/', views.purchases, name="purchases"),
  path('purchases/new/', views.purchases_new, name="purchases_new"),
  path('purchases/<int:pk>/', views.purchases_edit, name="purchases_edit"),
  path('purchases/remove/<int:pk>', views.purchases_remove, name="purchases_remove"),
  path('payments/', views.payments, name="payments"),
  path('payments/new/', views.payments_new, name="payments_new"),
  path('payments/<int:pk>/', views.payments_edit, name="payments_edit"),
  path('payments/remove/<int:pk>', views.payments_remove, name="payments_remove"),
]