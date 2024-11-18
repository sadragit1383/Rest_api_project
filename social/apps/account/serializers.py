"""
Serializers for managing user-related actions, including registration and activation.
"""

from rest_framework import serializers
from .models import Customuser


class UserSerializers(serializers.ModelSerializer):
    """
    Serializer for handling complete user data, including all fields in the Customuser model.
    """

    class Meta:
        model = Customuser
        fields = '__all__'


class RegisterSerializers(serializers.ModelSerializer):
    """
    Serializer for user registration, capturing only mobile number and password fields.
    """

    class Meta:
        model = Customuser
        fields = ['mobile_number', 'password']


class ActiveCodeSerializers(serializers.ModelSerializer):
    """
    Serializer for user activation code handling, limited to the active code field.
    """

    class Meta:
        model = Customuser
        fields = ['active_code']
