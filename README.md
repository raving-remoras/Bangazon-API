# Welcome to Bangazon

This API will give you access to resources about the Bangazon corporation, and all e-commerce data. It is powered by Django Rest Framework.

## Installation
- Create an empty directory to house your new project
- run `virtualenv env` to create a virtual environment within that directory
- run `source env/bin/activate` to initialize a virtual environment (`deactivate` to exit environment)
- run `git clone [repository id]`
- run `cd bangazon-API`
- run `pip install -r requirements.txt`

## Seed a Starter Database
- Run `python manage.py makemigrations api`
- Run `python manage.py migrate`
- If you want some data to play with, run `python manage.py loaddata db.json`
- Initialize the project using the command line by typing `python manage.py runserver` in the main directory.
- Access the application in a browser at `http://localhost:8000/api/v1`.

## Using the API
All calls to the API will be made from `http://localhost:8000/api/v1`
>EX you can get a list of all the customers by making a get call to `http://localhost:8000/api/v1/customer`
CORS is enabled with `http://www.bangazon.com`
To set your local host to `http://www.bangazon.com`
For Windows: Open `C:\Windows\System32\drivers\etc\hosts` as the Administrator Add 	`127.0.0.1:8080       www.bangazon.com` to the bottom of the document.
For Mac: in the console run
`sudo vim /etc/host`
Hit ‘i’ to enter Insert Mode, then put this at the bottom:
127.0.0.1:8080       www.bangazon.com
Press ‘esc’ to exit insert mode.
Write ‘:wq’ to exit vim

## Corporation Resources

### Department
<!-- * GET
    * GET All: You can access a list of all departments by submitting a GET request to `http://localhost:8000/api/v1/departments`
    * GET One: You can get the information of a single department by submitting a GET request to `http://localhost:8000/api/v1/departments/{departmentID}`
    * GET Departments & Employees: You can access a list of departments and their associated employees by submitting a GET request to `http://localhost:8000/api/v1/departments?_include=employees`
    * GET Departments with Budget over $300,000: You can access a list of all departments with budgets greater than $300,000 by submitting a GET request to `http://localhost:8000/api/v1/departments?_filter=budget&gt=300000` -->
<!-- * PUT
    * PUT Update Single Department: You can update a single department's information by submitting a PUT request to `http://localhost:8000/api/v1/departments/{departmentID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Department: You can post a new department by submitting a POST request to `http://localhost:8000/api/v1/departments` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->

### Employees
<!-- * GET
    * GET All: You can access a list of all employees, their associated department and current computer by submitting a GET request to `http://localhost:8000/api/v1/employees`
    * GET One: You can get the information of a single employee, their department and current computer by submitting a GET request to `http://localhost:8000/api/v1/employees/{employeeID}` -->
<!-- * PUT
    * PUT Update Single Employee: You can update a single employee's information by submitting a PUT request to `http://localhost:8000/api/v1/employees/{employeeID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Employee: You can post a new employee by submitting a POST request to `http://localhost:8000/api/v1/employees` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->

### Computers
<!-- * GET
    * GET All: You can access a list of all computers by submitting a GET request to `http://localhost:8000/api/v1/computers`
    * GET One: You can get the information of a single computer by submitting a GET request to `http://localhost:8000/api/v1/computers/{computerID}` -->
<!-- * PUT
    * PUT Update Single Computer: You can update a single computer's information by submitting a PUT request to `http://localhost:8000/api/v1/computers/{computerID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Computer: You can post a new computer by submitting a POST request to `http://localhost:8000/api/v1/computers` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->
<!-- * DELETE
    * DELETE Single Computer: You can delete a single computer from the databse by submitting a DELETE request to `http://localhost:8000/api/v1/computers/{computerID}` -->

### Training
* GET
    * GET All: You can access a list of all trainings and the employees that have signed up for the training session by submitting a GET request to `http://localhost:8000/api/v1/trainings`
    * GET One: You can get the information of a single training by submitting a GET request to `http://localhost:8000/api/v1/trainings/{trainingID}`
    * GET Future Training: You can access a list of all training programs starting today by submitting a GET request to `http://localhost:8000/api/v1/trainings/?completed=false`
* PUT
    * PUT Update Single Training: You can update a single training's information by submitting a PUT request to `http://localhost:8000/api/v1/trainings/{trainingID}`
        * You must submit the entire changed object which will include: `title`, `start_date`, `end_date`, `max_attendees`
* POST
    * POST New Training: You can post a new training by submitting a POST request to `http://localhost:8000/api/v1/trainings`
        * You must submit the entire changed object which will include: `title`, `start_date`, `end_date`, `max_attendees`
* DELETE
    * DELETE Single Training: You can only delete a training session that has not yet started. To delete an upcoming training session, submit a DELETE request to `http://localhost:8000/api/v1/trainings/{trainingID}`

## E-Commerce Resources

### Customer
<!-- * GET
    * GET All: You can access a list of all customers by submitting a GET request to `http://localhost:8000/api/v1/customers`
    * GET One: You can access the information on a single customer by submitting a GET request to `http://localhost:8000/api/v1/customers/{customerID}`
    * GET Active Customers: You can access all customers with an active order by submitting a GET request to `http://localhost:8000/api/v1/customers/?active=true`
    * GET Customers & Products: You can access all customers and the products they currently have for sale by submitting a GET request to `http://localhost:8000/api/v1/customers?_include=products`
    * GET Customers & Payment Types: You can access all customers and the payment types they have used to pay for an order by submitting a GET request to `http://localhost:8000/api/v1/customers?_include=payments`
    * GET Inactive Customers: You can access all customers that have NOT created an order by submitting a GET call to `http://localhost:8000/api/v1/customers/?active=false`
    * GET Search: You can search all fields of the customer table by submitting a GET request to `http://localhost:8000/api/v1/customers/?q={your-query}` -->
<!-- * PUT
    * PUT Update Single Customer: You can update a single customer's information by submitting a PUT request to `http://localhost:8000/api/v1/customers/{customerID}`
        * You must submit the entire changed object, which will include `customerID`, `first_name`, `last_name`, -->
  <!-- TODO: Come back to this one and list everything out -->
<!-- * POST
    * POST New Customer: You can post a new customer by submitting a POST request to `http://localhost:8000/api/v1/customers` -->
  <!-- TODO: Must add notes around what elements are required to be sent in with the request -->

### Products
<!-- * GET
    * GET All: You can access a list of all products by submitting a GET request to `http://localhost:8000/api/v1/products`
    * GET One: You can access the information of a single product by submitting a GET request to `http://localhost:8000/api/v1/products/{productID}` -->
<!-- * PUT
    * PUT Update Single Product: You can update a single product's information by submitting a PUT request to `http://localhost:8000/api/v1/products/{productID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Product: You can post a new product by submitting a POST request to `http://localhost:8000/api/v1/products` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->
<!-- * DELETE
    * DELETE Single Product: You can delete a single product from the databse by submitting a DELETE request to `http://localhost:8000/api/v1/products/{productID}` -->

### Product Type
<!-- * GET
    * GET All: You can access a list of all product types by submitting a GET request to `http://localhost:8000/api/v1/producttypes`
    * GET One: You can access the information of a single product type by submitting a GET request to `http://localhost:8000/api/v1/producttypes/{producttypeID}` -->
<!-- * PUT
    * PUT Update Single Product Type: You can update a single product type's information by submitting a PUT request to `http://localhost:8000/api/v1/producttypes/{producttypeID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Product Type: You can post a new product type by submitting a POST request to `http://localhost:8000/api/v1/producttypes` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->
<!-- * DELETE
    * DELETE Single Product Type: You can delete a single product type from the databse by submitting a DELETE request to `http://localhost:8000/api/v1/producttypes/{producttypeID}` -->

### Order
<!-- * GET
    * GET All: You can access a list of all orders by submitting a GET request to `http://localhost:8000/api/v1/orders`
    * GET One: You can access the information of a single order and it's associated products by submitting a GET request to `http://localhost:8000/api/v1/orders/{orderID}`
    * GET Open Orders: You can access a list of only open orders by submitting a GET request to `http://localhost:8000/api/v1/orders?completed=false`
    * GET Closed Orders: You can access a list of only closed orders by submitting a GET request to `http://localhost:8000/api/v1/orders?completed=true`
    * GET Orders & Products: You can access a list of all orders and their associated products by submitting a GET request to `http://localhost:8000/api/v1/orders?_include=products`
    * GET Orders & Customers: You can access a list of all orders and their associated customers by submitting a GET request to `http://localhost:8000/api/v1/orders?_include=customers` -->
<!-- * PUT
    * PUT Update Single Order: You can update a single order's information by submitting a PUT request to `http://localhost:8000/api/v1/orders/{orderID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Order: You can post a new order by submitting a POST request to `http://localhost:8000/api/v1/orders` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->
<!-- * DELETE
    * DELETE Single Order: You can delete a single order from the databse by submitting a DELETE request to `http://localhost:8000/api/v1/orders/{orderID}`
        * When an order is deleted, this will also remove all associated items in the Order Products table -->

### Payment Type
<!-- * GET
    * GET All: You can access a list of all payment types by submitting a GET request to `http://localhost:8000/api/v1/paymenttypes`
    * GET One: You can get the information of a single payment type by submitting a GET request to `http://localhost:8000/api/v1/paymenttypes/{paymenttypeID}` -->
<!-- * PUT
    * PUT Update Single Payment Type: You can update a single payment type's information by submitting a PUT request to `http://localhost:8000/api/v1/paymenttypes/{paymenttypeID}`
        * You must submit the entire changed object which will include: -->
  <!-- TODO: Update below list with all elements that need to be passed through -->
<!-- * POST
    * POST New Payment Type: You can post a new payment type by submitting a POST request to `http://localhost:8000/api/v1/paymenttypes` -->
  <!-- TODO: Must add notes around what elements are requred to be sent in with the request -->
<!-- * DELETE
    * DELETE Single Payment Type: You can delete a single payment type from the databse by submitting a DELETE request to `http://localhost:8000/api/v1/paymenttypes/{paymenttypeID}` -->
