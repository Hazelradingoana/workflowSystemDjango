from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    excel_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FinancialData(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    excel_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Financial Data for {self.customer} ({self.uploaded_at})"