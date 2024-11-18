"""
Views for user registration, authentication, and management.
"""

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login
import funcs
from .models import Customuser
from .serializers import RegisterSerializers

def return_response(message):
    """
    Helper function to return a standardized response message.
    """
    return Response({'message': message})


class ListUserGeneric(generics.ListCreateAPIView):
    """
    View to list all users or create a new user.
    Only accessible to admin users.
    """
    queryset = Customuser.objects.all()
    serializer_class = RegisterSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class ListUserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a user by ID.
    Only accessible to admin users.
    """
    queryset = Customuser.objects.all()
    serializer_class = RegisterSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]


class RegisterUserApiView(APIView):
    """
    API view to register a new user with a unique mobile number.
    """
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        """
        Register a new user if the mobile number is unique.
        """
        mobile_number = request.data.get('mobile_number')

        # Check for duplicate mobile number
        if Customuser.objects.filter(mobile_number=mobile_number).exists():
            return Response(
                {'message': 'این شماره موبایل قبلاً ثبت شده است.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = RegisterSerializers(data=request.data)
        if data.is_valid():
            user = data.save()
            random_code = funcs.create_random_code(5)
            user.active_code = random_code
            user.set_password(request.data.get('password'))
            user.save()

            request.session['user_info'] = {
                'mobile_number': user.mobile_number,
                'active_code': user.active_code,
                'remember_password': False
            }

            return Response(data.data, status=status.HTTP_201_CREATED)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class ActiveCodeGeneric(APIView):
    """
    API view to handle user activation through a verification code.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Verify the user's activation code and activate the user if correct.
        """
        user_info = request.session.get('user_info', {})
        user_code = request.data.get('active_code')
        mobile_number = user_info.get('mobile_number')
        user = get_object_or_404(Customuser, mobile_number=mobile_number)
        new_code = funcs.create_random_code(5)

        if int(user_code) == int(user_info.get('active_code')):
            if not user_info.get('remember_password'):
                user.is_active = True
                user.active_code = new_code
                user.save()
                return return_response('User is active.')
            return return_response('Ready for change.')

        return return_response('The active code is incorrect.')


class LoginUserGeneric(APIView):
    """
    API view to log in a user based on mobile number and password.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Authenticate and log in the user if the credentials are correct.
        """
        mobile_number = request.data.get('mobile_number')
        password = request.data.get('password')

        db_user = get_object_or_404(Customuser, mobile_number=mobile_number)
        user = authenticate(request, username=mobile_number, password=password)
        if user:
            if not db_user.is_admin:
                if db_user.is_active:
                    login(request, user)
                    return return_response('Successfully logged in.')
                return return_response('User is not active.')
            return return_response('User is an admin and cannot log in here.')

        return return_response('User information not found.')


class RememberPassword(APIView):
    """
    API view to initiate the password reset process.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Send a verification code to reset the password.
        """
        mobile_number = request.data.get('mobile_number')
        user = get_object_or_404(Customuser, mobile_number=mobile_number)
        random_number = funcs.create_random_code(5)
        user.active_code = random_number
        user.save()

        request.session['user_info'] = {
            'mobile_number': user.mobile_number,
            'active_code': user.active_code,
            'remember_password': True
        }
        return return_response('Confirm your mobile number.')


class ChangePassword(APIView):
    """
    API view to change a user's password after verification.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """
        Change the user's password if verified.
        """
        user_info = request.session.get('user_info', {})
        user = get_object_or_404(Customuser, mobile_number=user_info.get('mobile_number'))
        password = request.data.get('password')
        user.set_password(password)
        user.save()

        return return_response('Password changed successfully.')
