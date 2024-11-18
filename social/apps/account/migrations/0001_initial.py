# Generated by Django 5.1.1 on 2024-11-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('mobile_number', models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='ایمیل')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='نام')),
                ('family', models.CharField(blank=True, max_length=60, null=True, verbose_name='خانوادگی')),
                ('is_active', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='رمز عبور')),
                ('active_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='کد تایید')),
                ('gender', models.CharField(choices=[('True', 'مرد'), ('False', 'زن')], default='True', max_length=10)),
                ('is_admin', models.BooleanField(default=False, verbose_name='وضعیت ادمین')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
