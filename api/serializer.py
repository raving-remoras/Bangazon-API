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


class TrainingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Training
        fields = "__all__"


class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeTraining
        fields = "__all__"


class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        fields = "__all__"


class EmployeeComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeComputer
        fields = "__all__"


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


    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get("_include")
        q = request.query_params.get("q")

        if include == "products":
            self.fields["product"] = ProductSerializer(source="product_set", many=True, read_only=True)

        if include == "payments":
            self.fields["used_paymenttypes"] = PaymentTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = ("url", "first_name", "last_name", "email", "username", "street_address", "city", "state", "zipcode", "phone_number", "join_date", "delete_date")




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

