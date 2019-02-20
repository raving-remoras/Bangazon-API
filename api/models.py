import datetime

from django.db import models
from django.utils import timezone

### HR Models

class Department(models.Model):
    """Defines a department within the organization.

    Author: Sebastian Civarolo

    Returns:
        str -- Description of the employee and training relationship
    """

    name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Defines a past or present employee of the organization.

    Author: Sebastian Civarolo

    Returns:
        __str__ -- Full name, start and end date, and department
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    is_supervisor = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Full Name: {self.first_name} {self.last_name} Start Date: {self.start_date}"


class Training(models.Model):
    """Defines a class representing a training session being hosted by the company.

        Author: Kelly Morin

        Returns:
            str -- Training title, start and end date and maximum number of attendees
    """
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_attendees = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} training session is scheduled for {self.start_date} and ends {self.end_date}. It can hold a maximum of {self.max_attendees} attendees"


class EmployeeTraining(models.Model):
    """Defines a class representing a relationship between the employee and training sessions.

        Author: Kelly Morin

        Returns:
            str -- Description of the employee and training relationship
     """
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} is registered for {self.training}"


class Computer(models.Model):
    """Defines a class representing a computer purchased by the company.

        Author: Sebastian Civarolo

        Returns:
            str -- Make, Model and Serial No. of a computer
    """

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    purchase_date = models.DateTimeField()
    employee = models.ManyToManyField(Employee, through="EmployeeComputer")
    retire_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} - Serial No: {self.serial_no}"


class EmployeeComputer(models.Model):
    """Defines the assignment of a computer to an employee and records the start and end dates.

        Author: Sebastian Civarolo

        Returns:
            str -- Employee name and Make, Model, and Serial No. of computer assigned to them.
    """

    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    computer = models.ForeignKey(Computer, on_delete=models.PROTECT)
    date_assigned = models.DateTimeField()
    date_revoked = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}: {self.computer.make} {self.computer.model}, Serial No: {self.computer.serial_no}"


### E-commerce Models
class Customer(models.Model):
    """Defines a model for a customer, address, and phone number
        Author: Jase Hackman
        Returns: __str__ userId, street_address, and phone_number
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=50)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    join_date = models.DateTimeField(default=timezone.now)
    delete_date = models.DateTimeField(default=None, null=True, blank=True)


    def __str__(self):
        return f"First Name: {self.first_name} Last Name: {self.last_name} Address:{self.street_address} Phone: {self.phone_number}"


# Product Models
class ProductType(models.Model):
    """ Defines a product type.

        Author: Sebastian Civarolo

    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Defines a Product

        Author: God
    """
    seller = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    delete_date = models.DateTimeField(default=None, null=True, blank=True)
    local_delivery = models.BooleanField(default=False)
    delivery_city = models.CharField(max_length=30, blank=True, null=True, default=None)
    delivery_state = models.CharField(max_length=2, blank=True, null=True, default=None)

    def __str__(self):
        return f"Title: {self.title} Description:{self.description} Price:{self.price} Qty:{self.quantity}"


class PaymentType(models.Model):
    """Defines a payment type.


        Author:Jase Hackman

        Returns: PaymentType Name
    """
    name = models.CharField(max_length = 50)
    account_number = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    delete_date = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """ Defines an order

        Author: Rachel Daniel
        Methods: __str__ returns full name and completed (bool)
    """

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT, default=None, null=True, blank=True)
    payment_date = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f"Order: {self.id}, Customer Name: {self.customer.first_name} {self.customer.last_name}, Payment Type: {self.payment_type.name if self.payment_type else None}"


class OrderProduct(models.Model):
    """Defines the join table model for a product that is assigned to an order

        Author: Rachel Daniel
        Returns: __str__ productId and orderId

    """
    # cascade used here because open orders are hard deleted, so we want to remove join tables also
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product: {self.product} Order:{self.order}"