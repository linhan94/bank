from django.db import models

class Authentication(models.Model):
    accountNum = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    secureQuestion = models.CharField(max_length=512)
    secureAnswer = models.CharField(max_length=512)
    
    def __str__(self):
        return self.accountNum
	
class Item(models.Model):
    itemNum = models.IntegerField();
    name = models.CharField(max_length=512)
    price = models.FloatField(null=True)
    def __str__(self):
        return self.name

class WatchingHistory(models.Model):
    accountNum = models.CharField(max_length=128)
    wacthTime = models.DateTimeField(null=True)
    itemList = models.ManyToManyField(Item, symmetrical=False)
        
    def __str__(self):
        return self.accountNum
        
class ShoppingHistory(models.Model):
    accountNum = models.CharField(max_length=128)
    purchaseTime = models.DateTimeField(null=True)
    itemList = models.ManyToManyField(Item, symmetrical=False)
        
    def __str__(self):
        return self.accountNum

class ShoppingBag(models.Model):
    accountNum = models.CharField(max_length=128)
    item = models.ManyToManyField(Item, symmetrical=False)
    quantity = models.IntegerField(null=True)
       
    def __str__(self):
        return self.accountNum
	
class Account (models.Model):
    accountNum = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    authentication = models.OneToOneField(Authentication, related_name='account')
    #watchingHistory = models.OneToOneField(WatchingHistory, related_name='account')
    #watchingHistory = models.ForeignKey(WatchingHistory, on_delete=models.CASCADE)
    watchingHistory = models.ManyToManyField(WatchingHistory, symmetrical=False)
    #shoppingHistory = models.OneToOneField(ShoppingHistory, related_name='account')
    shoppingHistory = models.ManyToManyField(ShoppingHistory, symmetrical=False)
    shoppingBag = models.OneToOneField(ShoppingBag, related_name='account')
    def __str__(self):
        return self.accountNum
	
