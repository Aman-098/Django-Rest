from rest_framework import serializers
from .models import Company,Employee  # Import the Company model

# Create serializer
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    comapny_id=serializers.ReadOnlyField()
    class Meta:
        model = Company  # Corrected to use '=' instead of ':'
        fields = "__all__"  # This will include all fields from the model


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"
