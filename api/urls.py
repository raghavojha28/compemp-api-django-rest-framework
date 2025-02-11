from django.urls import path, include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet

#define urlpatterns here

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]