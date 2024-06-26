# Workflow System Django

## Project Overview

Purpose
The purpose of this project is to build a simple, extensible web-based workflow system that captures customer information through an HTML form and processes an uploaded Excel file containing financial data. The system then renders a temporal graph showing the customer's income and expenditure over the last 12 months.

## Features
Customer Information Form: Users can enter a customer's first name, last name, and date of birth.
File Upload: Users can upload an Excel file with financial data for the last 12 months.
Graph Rendering: The system processes the uploaded Excel file and generates a graph showing the customer's income and expenditure over time.


## Technologies Used
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Pandas: A powerful data analysis and manipulation library for Python.
Openpyxl: A library for reading and writing Excel files.


## Key Components
views.py: Contains the logic for handling form submissions and file uploads.
urls.py: Maps URLs to the appropriate views.
templates/customers: Contains the HTML templates for the forms and the home page.


## How It Works

## Workflow

## Home Page:

Users navigate to the home page, where they see a form for entering customer information and uploading an Excel file.

![Home Page Screenshot](images/images/Screenshot 2024-06-27 004521.png)


## Form Submission:

When the form is submitted, the data is sent to the server, where it is processed by Django views.

![Home Page Screenshot](images/images/Screenshot 2024-06-27 004609.png)


## File Upload:

The uploaded Excel file is read using Pandas and Openpyxl.

![Home Page Screenshot](images/images/Screenshot 2024-06-27 004624.png)


## Data Processing:

The financial data is extracted from the Excel file and processed to generate a temporal graph.

## Graph Rendering:

The processed data is then used to render a graph showing the customer's income and expenditure over the last 12 months.

## Setting Up and Running the Project

## Prerequisites
Python 3.x
PostreSQL
Django
Git


## Steps to Run the Project

Clone the Repository:

git clone https://github.com/Hazelradingoana/workflowSystemDjango.git
cd workflowSystemDjango


## Create a Virtual Environment (Optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## Install the Required Packages:

pip install -r requirements.txt
## Apply Migrations:

python manage.py migrate

## Run the Development Server:

python manage.py runserver

![Home Page Screenshot](images/images/Screenshot 2024-06-27 004503.png)


## Access the Application:

Open a web browser and navigate to http://127.0.0.1:8000/
Fill out the customer information form and upload the Excel file.
Submit the form to see the generated temporal graph.


## Extending the Workflow

The workflow is designed to be extensible. To add new features or modify existing ones, follow the existing code structure and conventions. Use Django's built-in functionality for creating forms, handling file uploads, and rendering templates.

## License









## Features

- Capture customer information via an HTML form.
- Upload an Excel file with the customer's financial data.
- Render a temporal graph displaying income and expenditure.

## Assumptions

- The system supports only one user, without the need for login or user management.
- Data storage is implemented using SQLite for simplicity.
- The user interface is simple and styled using HTML forms.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- Pandas
- Openpyxl
-postgresSQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Hazelradingoana/workflowSystemDjango.git


Navigate to the project directory:


cd workflowSystemDjango


Install the required packages:

pip install -r requirements.txt


Run the migrations:

python manage.py migrate


Start the development server:

python manage.py runserver


Usage
Navigate to the home page and then get to the upload page.
fill out the customer form.
Upload the Excel file with financial data.
View the generated temporal graph displaying the customer's income and expenditure