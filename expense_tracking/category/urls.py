from django.urls import path,include
from rest_framework.routers import DefaultRouter
from category.views import CategoryView,PaymentView,ExpenseView

router = DefaultRouter()

router.register('category', CategoryView, basename='category')
router.register('payment', PaymentView, basename='payment')
router.register('expense', ExpenseView, basename='expense')


urlpatterns = [
   path('',include(router.urls))
]
