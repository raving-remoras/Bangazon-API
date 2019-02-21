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

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    product=ProductSerializer(read_only=True)


    class Meta:
        model = OrderProduct
        fields = ("product",)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    This Serializer is for Orders. Includes conditional fields if the correct keywords are added to the url.

    Models: Order, Product, OrderProducts

    Views: OrderViewSet

    Author(s): Jase Hackman
    """


    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        keyword = request.query_params.get('_include', None)
        print("kwards", kwargs)
        if 'instance' in kwargs:
            # instance is what is sent in kwargs when user request just one object.
            print(kwargs['instance'])
        elif(keyword=="customers"):
            self.fields['customer']=CustomerSerializer(read_only=True)

        elif(keyword=="products"):
            self.fields['product']=OrderProductSerializer(source="orderproduct_set", many = True, read_only=True)


    class Meta:
        model = Order
        fields = ("customer", "payment_type", "payment_date", "url")



class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    This Serializer is for getting back a single order.

    Models: Order, Product, OrderProducts

    Views: OrderViewSet

    Author(s): Jase Hackman
    """

    product=OrderProductSerializer(source="orderproduct_set", many = True, read_only=True)

    class Meta:
        model = Order
        fields = ( "payment_type", "payment_date", "url", "product")
