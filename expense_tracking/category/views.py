from rest_framework import viewsets
from category.models import Category,Payment,Expense
from category.serializers import CategorySerializer,PaymentSerializer,ExpenseSerializers
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

def home(request):
    pass

class CategoryView(viewsets.ModelViewSet):
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes=[SessionAuthentication,TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    http_method_names = ["get","post","put","delete"]

class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class=PaymentSerializer
    http_method_names=["get","post","put","delete"]

class ExpenseView(viewsets.ModelViewSet):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializers
    http_method_names=["get","post","put","delete"]

