from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
  name = models.CharField(max_length=50)
  identifier = models.CharField(max_length=100)
  account = models.DecimalField(max_digits=6, decimal_places=2)
  creation_date = models.DateTimeField(default=timezone.now)

  def registerPurchase(self, value):
    self.account += value
    self.save()

  def updatePurchase(self, oldValue):
    self.account -= oldValue
    self.save()
  
  def registerPayment(self, value):
    self.account -= value
    self.save()

  def updatePayment(self, oldValue):
    self.account += oldValue
    self.save()

  
class Purchase(models.Model):
  description = models.TextField()
  date = models.DateField()
  value = models.DecimalField(max_digits=6, decimal_places=2)
  client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

  def buy(self):
    self.date = timezone.now()
    self.save()

  def getValue(self):
    return self.value

class Payment(models.Model):
  method = models.CharField(max_length=10)
  date = models.DateField()
  value = models.DecimalField(max_digits=6, decimal_places=2)
  client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

  def pay(self):
    self.date = timezone.now()
    self.save()

  def getValue(self):
    return self.value
  