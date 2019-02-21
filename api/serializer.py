from rest_framework import serializers
from api.models import *


# HR Serializers

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = EmployeeTraining
        fields = ('employee',)

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    employees=EmployeeTrainingSerializer(source="employeetraining_set", many=True, read_only=True)

    class Meta:
        model = Training
        fields = ('id', 'title', 'start_date', 'end_date', 'max_attendees', 'employees')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        fields = "__all__"


class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeComputer
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

