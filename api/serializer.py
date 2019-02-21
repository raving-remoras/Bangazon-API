from rest_framework import serializers
from api.models import *


# HR Serializers

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

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

    class Meta:
        model = EmployeeComputer
        exclude = ('employee', )


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    department = EmployeeDepartmentSerializer(read_only=True)
    current_computer = CurrentEmployeeComputerSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "start_date", "end_date", "is_supervisor", "department", "current_computer",)


class TrainingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Training
        fields = "__all__"


class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeTraining
        fields = "__all__"


# E-Commerce Serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = "__all__"


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrderProduct
        fields = "__all__"

