from rest_framework import serializers
from category.models import Category,Payment,Expense


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields="__all__"
        
class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Payment
        fields="__all__"

class ExpenseSerializers(serializers.ModelSerializer):

    class Meta:
        model=Expense
        fields="__all__"