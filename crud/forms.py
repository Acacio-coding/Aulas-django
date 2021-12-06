from django import forms
from .models import Client, Purchase, Payment

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = ('name', 'identifier', 'account')

class PurchaseForm(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = ('client_id', 'description', 'value')

class PaymentForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = ('client_id', 'method', 'value')