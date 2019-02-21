from django.shortcuts import render
# from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

from api.models import Employee, Computer, Department, Training, EmployeeTraining, EmployeeComputer, Customer, ProductType, Product, PaymentType, Order, OrderProduct

from api.serializer import EmployeeSerializer, ComputerSerializer, DepartmentSerializer, TrainingSerializer, EmployeeTrainingSerializer, EmployeeComputerSerializer, CustomerSerializer, ProductTypeSerializer, ProductSerializer, PaymentTypeSerializer, OrderSerializer, OrderProductSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "computers": reverse("computers", request=request, format=format),
        "departments": reverse("departments", request=request, format=format),
        "employees": reverse("employees", request=request, format=format),
        "trainings": reverse("trainings", request=request, format=format),
        "employeecomputers": reverse("employeeComputer", request=request, format=format),
        "customers": reverse("customer", request=request, format=format),
        "producttypes": reverse("productType", request=request, format=format),
        "products": reverse("products", request=request, format=format),
        "orders": reverse("orders", request=request, format=format),
        "paymenttypes": reverse("paymenttypes", request=request, format=format),
        "orderproducts": reverse("orderproducts", request=request, format=format)
    })


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class EmployeeTrainingViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTraining.objects.all()
    serializer_class = EmployeeTrainingSerializer


class EmployeeComputerViewSet(viewsets.ModelViewSet):
    queryset = EmployeeComputer.objects.all()
    serializer_class = EmployeeComputerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        query_set = Order.objects.all()

        print(self.request.query_params)
        keyword = self.request.query_params.get('complete', None)
        if keyword == "false":
            print("query params", keyword)
            query_set = Order.objects.filter(payment_date=None)
        if keyword == "true":
            print("query params", keyword)
            query_set = Order.objects.exclude(payment_date__isnull=True)
        return query_set

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("instance", instance)
        if instance.payment_date == None:
            toDelete = instance.orderproduct_set.all()
            print("products!!!!!!", toDelete)
            for product in toDelete:
                product.delete()
            instance.delete()
        else:
            content = {'Error': 'Orders that have been completed cannot be removed'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer