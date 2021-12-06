from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Client, Purchase, Payment
from django.contrib.auth.models import User
from .forms import ClientForm, PurchaseForm, PaymentForm

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'app/dashboard.html', {})

@login_required
def clients(request):
  clients = Client.objects.order_by('name')
  return render(request, 'app/clients.html', {'clients' : clients})

@login_required
def clients_new(request):
  if request.method == "POST":
    form = ClientForm(request.POST)
    if form.is_valid():
      client = form.save(commit=False)
      client.creation_date = timezone.now();
      client.save()
      return redirect('clients')
  else:
    form = ClientForm()
    return render(request, 'app/clients_operation.html', {'form' : form})  

@login_required
def clients_edit(request, pk):
  client = get_object_or_404(Client, pk=pk)
  if request.method == "POST":
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
      client = form.save(commit=False)
      client.creation_date = timezone.now();
      client.save()
      return redirect('clients')
  else:
    form = ClientForm(instance=client)
    return render(request, 'app/clients_operation.html', {'form': form})

@login_required
def detalhes_cliente(request, pk):
  client = get_object_or_404(Client, pk=pk)
  purchases = Purchase.objects.filter("client_id" == client.id)
  return render(request, 'app/detalhes_cliente.html', {'client' : client, 'purchases' : purchases})

@login_required
def clients_remove(request, pk):
  client = get_object_or_404(Client, pk=pk)
  client.delete()
  return redirect('clients')

@login_required
def purchases(request):
  purchases = Purchase.objects.order_by('date')
  return render(request, 'app/purchases.html', {'purchases' : purchases})

@login_required
def purchases_new(request):
  if request.method == "POST":
    form = PurchaseForm(request.POST)
    if form.is_valid():
      purchase = form.save(commit=False)
      purchase.buy()
      client = get_object_or_404(Client, pk=purchase.client_id.id)
      client.registerPurchase(purchase.value);
      return redirect('purchases')
  else:
    form = PurchaseForm()
    return render(request, 'app/purchases_operation.html', {'form' : form})  

@login_required
def purchases_edit(request, pk):
  purchase = get_object_or_404(Purchase, pk=pk)
  oldValue = purchase.getValue()
  if request.method == "POST":
    form = PurchaseForm(request.POST, instance=purchase)
    if form.is_valid():
      purchase = form.save(commit=False)
      client = get_object_or_404(Client, pk=purchase.client_id.id)
      client.updatePurchase(oldValue)
      purchase.buy()
      client.registerPurchase(purchase.value);
      return redirect('purchases')
  else:
    form = PurchaseForm(instance=purchase)
    return render(request, 'app/purchases_operation.html', {'form' : form})  

@login_required
def purchases_remove(request, pk):
  purchase = get_object_or_404(Purchase, pk=pk)
  purchase.delete()
  return redirect('purchases')

@login_required
def payments(request):
  payments = Payment.objects.order_by('date')
  return render(request, 'app/payments.html', {'payments' : payments})

@login_required
def payments_new(request):
  if request.method == "POST":
    form = PaymentForm(request.POST)
    if form.is_valid():
      payment = form.save(commit=False)
      payment.pay()
      client = get_object_or_404(Client, pk=payment.client_id.id)
      client.registerPayment(payment.value);
      return redirect('payments')
  else:
    form = PaymentForm()
    return render(request, 'app/payments_operation.html', {'form' : form})  

@login_required
def payments_edit(request, pk):
  payment = get_object_or_404(Payment, pk=pk)
  oldValue = payment.getValue()
  if request.method == "POST":
    form = PaymentForm(request.POST, instance=payment)
    if form.is_valid():
      payment = form.save(commit=False)
      client = get_object_or_404(Client, pk=payment.client_id.id)
      client.updatePayment(oldValue)
      payment.pay()
      client.registerPayment(payment.value);
      return redirect('payments')
  else:
    form = PaymentForm(instance=payment)
    return render(request, 'app/payments_operation.html', {'form' : form})

@login_required
def payments_remove(request, pk):
  payment = get_object_or_404(Payment, pk=pk)
  payment.delete()
  return redirect('payments')