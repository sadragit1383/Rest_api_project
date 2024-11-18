from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
import funcs
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self,mobile_number,gender='',password=None,email='',active_code='',name='',family=''):
        user  = self.model(
            mobile_number = mobile_number,
            gender = gender,
            name = name,
            family = family,
            active_code = active_code,
            password = password,
            email = email,
        )

        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,mobile_number,email,password,name,family,gender='',active_code='',):

        user = self.create_user(
            mobile_number = mobile_number,
            name = name,
            family = family,
            password = password,
            email = email,
            gender= gender,
            active_code=active_code
        )


        user.is_admin = True
        user.is_superuser = True
        user.is_active = True

        user.save(using = self.db)
        return user


# modal of user

class Customuser(AbstractBaseUser,PermissionsMixin):
    mobile_number = models.CharField(max_length=11,verbose_name='شماره موبایل',unique=True)
    email = models.EmailField(max_length=100,verbose_name='ایمیل',blank=True,null=True)
    name = models.CharField(max_length=60,verbose_name='نام',blank=True,null=True)
    family = models.CharField(max_length=60,verbose_name='خانوادگی',blank=True,null=True)
    is_active = models.BooleanField(default=False,verbose_name='وضعیت',blank=True,null=True)
    password = models.CharField(max_length=100,verbose_name='رمز عبور',blank=True,null=True)
    active_code = models.CharField(max_length=16,verbose_name='کد تایید',blank=True,null=True)
    GENDER_LIST = (('True','مرد'),('False','زن'))
    gender = models.CharField(max_length=10,choices=GENDER_LIST,default='True')
    is_admin = models.BooleanField(default=False,verbose_name='وضعیت ادمین',)


    objects = CustomUserManager()
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['name','email','family']


    @property
    def is_staff(self):
        return self.is_admin

#====================================
