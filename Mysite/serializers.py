from rest_framework import serializers
from .models import Employee

class Employeeserialiers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields=(' eid','ename','eemail','econtact')
