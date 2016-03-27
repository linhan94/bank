from rest_framework import serializers
from .models import Account, Authentication, Item, ShoppingBag,WatchingHistory, ShoppingHistory

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    # authentication = serializers.HyperlinkedRelatedField(
        # many=False,
        # read_only=True,
        # view_name='account-authentication'
    # )
    # watchingHistory = serializers.HyperlinkedRelatedField(
        # many=True,
        # read_only=True,
        # view_name='account-watchingHistory'
    # )
    # shoppingHistory = serializers.HyperlinkedRelatedField(
        # many=True,
        # read_only=True,
        # view_name='account-shoppingHistory'
    # )
    class Meta:
        model = Account
        fields = ('accountNum','name', 'address','authentication','watchingHistory', 'shoppingHistory', 'shoppingBag')

class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authentication
        fields = ('accountNum', 'email','password','secureQuestion','secureAnswer')
	  
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('itemNum', 'name','price')        
        
class WatchingHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WatchingHistory
        fields = ('accountNum','wacthTime','itemList')
        
class ShoppingHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingHistory
        fields = ('accountNum','purchaseTime','itemList')
		
class ShoppingBagSerializer(serializers.HyperlinkedModelSerializer):
    # account = serializers.HyperlinkedRelatedField(
        # many=False,
        # read_only=True,
        # view_name='account-shoppingBag'
    # )
    class Meta:
        model = ShoppingBag
        fields = ('accountNum','item', 'quantity')