from rest_framework import serializers
from .models import Appointment, Category, Service
from django.contrib.auth import get_user_model
User = get_user_model()


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'appointment_date', 'services', 'user')
        extra_kwargs = {
            'services': {'required': False}
        }


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category')


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'service_name', 'delivery_time',
                  'private_price', 'business_price')


class PopulateServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Service
        fields = ('id', 'service_name', 'delivery_time',
                  'private_price', 'business_price', 'category')


class PopulateCategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'category', 'services')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'age', 'phone_number', 'user_type')


class PopulateAppointmentSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Appointment
        fields = ('id', 'appointment_date', 'user', 'services')
