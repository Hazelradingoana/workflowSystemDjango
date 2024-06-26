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

![Screenshot 2024-06-27 004521](https://github.com/Hazelradingoana/workflowSystemDjango/assets/125089769/d9b476c2-3221-4c6d-9d48-d916dc05ac2a)


## Form Submission:

When the form is submitted, the data is sent to the server, where it is processed by Django views.

![Screenshot 2024-06-27 004609](https://github.com/Hazelradingoana/workflowSystemDjango/assets/125089769/7af32ec6-7a3c-40e7-9817-f4893227fc07)


## File Upload:

The uploaded Excel file is read using Pandas and Openpyxl.

![Screenshot 2024-06-27 004609](https://github.com/Hazelradingoana/workflowSystemDjango/assets/125089769/7af32ec6-7a3c-40e7-9817-f4893227fc07)

## Data Processing:

The financial data is extracted from the Excel file and processed to generate a temporal graph.

![Screenshot 2024-06-27 004624](https://github.com/Hazelradingoana/workflowSystemDjango/assets/125089769/1cc50089-c8b3-40d9-986f-01558078a61e)


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

![Screenshot 2024-06-27 004503](https://github.com/Hazelradingoana/workflowSystemDjango/assets/125089769/0f08e2a0-fd61-4f1a-89cf-934b19fca6ca)


## Access the Application:

Open a web browser and navigate to http://127.0.0.1:8000/
Fill out the customer information form and upload the Excel file.
Submit the form to see the generated temporal graph.


## Extending the Workflow

The workflow is designed to be extensible. To add new features or modify existing ones, follow the existing code structure and conventions. Use Django's built-in functionality for creating forms, handling file uploads, and rendering templates.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- Pandas
- Openpyxl
-postgreSQL


## Usage
Navigate to the home page and then get to the upload page.
fill out the customer form.
Upload the Excel file with financial data.
View the generated temporal graph displaying the customer's income and expenditure
