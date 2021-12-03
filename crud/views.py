from django.shortcuts import render

# Create your views here.
def login(request):
  return render(request, 'app/login.html', {})

def dashboard(request):
  return render(request, 'app/dashboard.html', {})

def clients(request):
  return render(request, 'app/clients.html', {})

def purchases(request):
  return render(request, 'app/purchases.html', {})

def payments(request):
  return render(request, 'app/payments.html', {})