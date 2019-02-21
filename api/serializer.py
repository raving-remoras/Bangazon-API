from rest_framework import serializers
from api.models import *


# HR Serializers

class BasicEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """ Employee serializer used by DepartmentSerializer to display current employees so department field is excluded on Employee.

    Author: Sebastian Civarolo
    """

    class Meta:
        model = Employee
        exclude = ("department",)


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """ Displays departments with option to include employees.

    Author: Sebastian Civarolo

    Params:
        _include=employees -- optionally display all employees in department.
    """

    def __init__(self, *args, **kwargs):
        super(DepartmentSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get("_include", None)

        if include == "employees":
            self.fields["employees"] = BasicEmployeeSerializer(source="employee_set", many=True, read_only=True)

    class Meta:
        model = Department
        fields = "__all__"


class EmployeeDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """On employee, department info is displayed without budget

    Author: Sebastian Civarolo
    """

    class Meta:
        model = Department
        exclude = ("budget",)


class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        fields = "__all__"


class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):
    computer = ComputerSerializer()

    class Meta:
        model = EmployeeComputer
        fields = "__all__"


class CurrentComputerSerializer(serializers.HyperlinkedModelSerializer):
    """Custom Computer Serializer for displaying relevant data for an employee's current_computer

    Author: Sebastian Civarolo
    """

    class Meta:
        model = Computer
        fields = ("url", "make", "model", "serial_no")


class CurrentEmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):
    """Custom EmployeeComputer serializer for use when EmployeeComputer is being used for current_computer on Employee

    Author: Sebastian Civarolo
    """

    computer = CurrentComputerSerializer()

    class Meta:
        model = EmployeeComputer
        exclude = ('employee', )


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    department = EmployeeDepartmentSerializer(read_only=True)
    current_computer = CurrentEmployeeComputerSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "start_date", "end_date", "is_supervisor", "department", "current_computer", "url")


class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):
    employee = BasicEmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeTraining
        fields = ('employee',)


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    employees=EmployeeTrainingSerializer(source="employeetraining_set", many=True, read_only=True)

    class Meta:
        model = Training
        fields = ('id', 'title', 'start_date', 'end_date', 'max_attendees', 'employees')


# E-Commerce Serializers
class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class UsedPaymentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = "__all__"


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """ Converts Customer model into viewable Data. Specifies search parameters of "_include=products" and "_include=payments"

        Author: Rachel Daniel
    """

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get("_include")
        print(include)

        if "products" in include:
            self.fields["product"] = ProductSerializer(source="product_set", many=True, read_only=True)

        if "payments" in include:
            self.fields["used_paymenttypes"] = PaymentTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = ("url", "first_name", "last_name", "email", "username", "street_address", "city", "state", "zipcode", "phone_number", "join_date", "delete_date")


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = "__all__"



class CustomerExtraSerializer(serializers.HyperlinkedModelSerializer):
    """ Converts Customer model into viewable Data.

        Models: Customer

        Views: none

        Author: Jase Hackman
    """
    class Meta:
        model = Customer
        fields = ("url", "first_name", "last_name", "email", "username", "street_address", "city", "state", "zipcode", "phone_number", "join_date", "delete_date")


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    This Serializer is for Orders. Includes conditional fields if the correct keywords are added to the url.

    Models: Order, Product, OrderProducts

    Views: OrderViewSet

    Author(s): Jase Hackman
    """


    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        if "context" in kwargs:
            request = kwargs['context']['request']
            keyword = request.query_params.get('_include', None)
            print("kwards", kwargs)
            # if 'instance' in kwargs:
            #     # instance is what is sent in kwargs when user request just one object.
            #     print(kwargs['instance'])
            if(keyword=="customers"):
                self.fields['customer']=CustomerExtraSerializer(read_only=True)

            if(keyword=="products"):
                self.fields['products']=OrderProductSerializer(source="orderproduct_set", many = True, read_only=True)


    class Meta:
        model = Order
        fields = ("customer", "payment_type", "payment_date", "url")


class OrderProductViewSerializer(serializers.HyperlinkedModelSerializer):
    product=ProductSerializer(read_only=True)
    order=OrderSerializer(read_only=True)


    class Meta:
        model = OrderProduct
        fields = ("product", "order")

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    product=ProductSerializer(read_only=True)


    class Meta:
        model = OrderProduct
        fields = ("product", )


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    This Serializer is for getting back a single order.

    Models: Order, Product, OrderProducts

    Views: OrderViewSet

    Author(s): Jase Hackman
    """

    products=OrderProductSerializer(source="orderproduct_set", many = True, read_only=True)

    class Meta:
        model = Order
        fields = ( "payment_type", "payment_date", "url", "products")

