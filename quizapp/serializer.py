from rest_framework import serializers
from .models import *
class BookSerializer(serializers.ModelSerializer):
    author_name=serializers.SerializerMethodField()

    class Meta:
        model=Book
        fields=("title","author","author_name")

    def get_author_name(self,obj):
        return obj.author.name
    

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']


class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True, source='employee_set')

    class Meta:
        model = Company
        fields = ['id', 'name', 'employees']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user