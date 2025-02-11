from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

# Create your views here.

    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

    #defining view for custom endpoints here: companies/{company_id}/employees

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        
        except:
            return Response('message: company might not exists!!')
        

    @action(detail=False, methods=['POST'])
    def createcompany(self, request):
        print('method allowed')
        return Response({'message': 'Custom POST action executed successfully.'})

    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

