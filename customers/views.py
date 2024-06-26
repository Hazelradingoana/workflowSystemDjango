# customers/views.py

from django.shortcuts import render, redirect
from .models import Customer, FinancialData
from .forms import CustomerForm, FileUploadForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        file_form = FileUploadForm(request.POST, request.FILES)
        if customer_form.is_valid() and file_form.is_valid():
            # Save customer information
            customer = customer_form.save()

            # Save uploaded file information
            financial_data = file_form.save(commit=False)
            financial_data.customer = customer
            financial_data.save()

            # Process Excel file to render temporal graph
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            # Process data and render temporal graph (example)
            # Assuming df contains financial data for the last 12 months
            plt.plot(df['Month'], df['Income'], label='Income')
            plt.plot(df['Month'], df['Expenses'], label='Expenses')
            plt.xlabel('Month')
            plt.ylabel('Amount')
            plt.title(f'Financial Data for {customer}')
            plt.legend()
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            graph = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close()

            return render(request, 'customers/graph.html', {'customer': customer, 'graph': graph})

    else:
        customer_form = CustomerForm()
        file_form = FileUploadForm()
    
    return render(request, 'customers/upload.html', {'customer_form': customer_form, 'file_form': file_form})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    financial_data = FinancialData.objects.filter(customer=customer).last()  # Assuming latest upload
    return render(request, 'customers/customer_detail.html', {'customer': customer, 'financial_data': financial_data})


def home(request):
    return render(request, 'customers/home.html')  # Replace with your actual home template name
