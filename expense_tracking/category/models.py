from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# For Category API
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table="category"

# For Payment API
class Payment(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table="payment"

# For Expense API
class Expense(models.Model):
   amount=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10000)])
   spenddate=models.DateField()
   purpose=models.CharField(max_length=30)
   category=models.ForeignKey(Category,on_delete=models.CASCADE)
   payment=models.ForeignKey(Payment,on_delete=models.CASCADE)

   def __str__(self) -> str:
    return f"Amount: {self.amount}Spend Date: {self.spenddate}<br>Purpose: {self.purpose}<br>Category: {self.category}<br>Payment: {self.payment}"

   class Meta:
       db_table="expense"






