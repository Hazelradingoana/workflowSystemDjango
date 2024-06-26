# customers/forms.py

from django import forms
from .models import Customer, FinancialData

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'date_of_birth']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FinancialData
        fields = ['excel_file']
