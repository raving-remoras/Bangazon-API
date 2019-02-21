from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import status
from api.models import Employee, Computer, Department, Training, EmployeeTraining, EmployeeComputer, Customer, ProductType, Product, PaymentType, Order, OrderProduct
from api.serializer import EmployeeSerializer, ComputerSerializer, DepartmentSerializer, TrainingSerializer, EmployeeTrainingSerializer, EmployeeComputerSerializer, CustomerSerializer, ProductTypeSerializer, ProductSerializer, PaymentTypeSerializer, OrderSerializer, OrderProductSerializer, OrderDetailSerializer

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
    """ Defines the views for the Department resource.

    Author: Sebastian Civarolo
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ("get", "post", "put", "options")

    def get_queryset(self):
        """ Optionally restricts the returned departments by budget greater than specified amount.

        example: ?_filter=budget&_gt=300000
        """

        queryset = Department.objects.all()
        _filter = self.request.query_params.get("_filter", None)
        _gt = self.request.query_params.get("_gt", None)

        if _filter == "budget" and _gt is not None:
            queryset = queryset.filter(budget__gt=_gt)

        return queryset


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ("get", "post", "put", "options")


class TrainingViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    filter_fields=('start_date',)
    today = datetime.now()

    def get_queryset(self):
        completed = self.request.query_params.get('completed', None)
        if completed is not None:
            if completed == "false":
                queryset = Training.objects.filter(start_date__date__gte=self.today).order_by("start_date")
            elif completed == "true":
                queryset = Training.objects.filter(end_date__date__lte=self.today).order_by("start_date")
            else:
                queryset = Training.objects.all()
        else:
            queryset = Training.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.start_date >= self.today:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            content = {'Error': 'Training sessions that have been completed cannot be removed'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EmployeeTrainingViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTraining.objects.all()
    serializer_class = EmployeeTrainingSerializer


class EmployeeComputerViewSet(viewsets.ModelViewSet):
    queryset = EmployeeComputer.objects.all()
    serializer_class = EmployeeComputerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ["get", "post", "put", "options"]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("first_name", "last_name", "email", "username", "street_address", "city", "state", "zipcode", "phone_number", "join_date", "delete_date")


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        today = datetime.now()
        instance = self.get_object()
        instance.delete_date = today
        instance.save()


class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    This ViewSet deals with Post, Update, Get, and Delete for Orders

    Models: Order, OrderProducts

    Serializers: OrderSerializer

    Author(s): Jase Hackman
    """

    def get_serializer_class(self):
        # determins which serializer will be used for which type of request
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    queryset = Order.objects.all()

    def get_queryset(self):
        # If a user includes /?complete=true or /?complete=false the query will filter based on those conditions
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
        # If an order is not completed it will delete and the OrderProduct relationships will also delete. If it is completed it will raise an error.
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