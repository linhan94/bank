from django.shortcuts import render

from .models import Account, Authentication, Item, ShoppingBag, WatchingHistory, ShoppingHistory

# REST imports
from rest_framework import viewsets
from .serializers import AccountSerializer, AuthenticationSerializer, ItemSerializer, ShoppingBagSerializer, WatchingHistorySerializer, ShoppingHistorySerializer

class AccountViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating account
    queryset = Account.objects.order_by('accountNum')
    serializer_class = AccountSerializer

class AuthenticationViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating authentication
    queryset = Authentication.objects.order_by('accountNum')
    serializer_class = AuthenticationSerializer
	
class ItemViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating item
    queryset = Item.objects.order_by('itemNum')
    serializer_class = ItemSerializer
	
class WatchingHistoryViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating watching history
    queryset = WatchingHistory.objects.order_by('accountNum')
    serializer_class = WatchingHistorySerializer
    
class ShoppingHistoryViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating shopping history
    queryset = ShoppingHistory.objects.order_by('accountNum')
    serializer_class = ShoppingHistorySerializer
	
class ShoppingBagViewSet(viewsets.ModelViewSet):
    # API endpoint for listing and creating shopping bag
    queryset = ShoppingBag.objects.order_by('accountNum')
    serializer_class = ShoppingBagSerializer
