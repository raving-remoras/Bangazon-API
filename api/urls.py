from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
# HR
router.register('departments', views.DepartmentViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('trainings', views.TrainingViewSet)
router.register('employeetrainings', views.EmployeeTrainingViewSet)
router.register('computers', views.ComputerViewSet)
router.register('employeecomputers', views.EmployeeComputerViewSet)

# E-com
router.register('customers', views.CustomerViewSet)
router.register('products', views.ProductViewSet)
router.register('productsexpand', views.ProductExpandViewSet)
router.register('producttypes', views.ProductTypeViewSet)
router.register('paymenttypes', views.PaymentTypeViewSet)
router.register('orders', views.OrderViewSet)
router.register('orderproducts', views.OrderProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]