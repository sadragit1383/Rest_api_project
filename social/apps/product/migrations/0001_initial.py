# Generated by Django 5.1.1 on 2024-11-14 17:28

import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
import funcs
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200, verbose_name='Brand name')),
                ('slug', models.CharField(max_length=100, verbose_name='slug url')),
                ('image_name', models.ImageField(upload_to=funcs.FileUpload.upload_to, verbose_name='brand image')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Confirm time!')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('is_active', models.BooleanField(default=True, verbose_name='status of brand')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=100, verbose_name='Feature name')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_title', models.CharField(max_length=100, verbose_name='title')),
                ('english_value', models.CharField(blank=True, max_length=20, null=True, verbose_name='feature')),
                ('feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feature_value', to='product.feature', verbose_name='feature')),
            ],
            options={
                'verbose_name': 'Feature value',
                'verbose_name_plural': 'Feature Values',
            },
        ),
        migrations.CreateModel(
            name='GroupProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, verbose_name='Group Name')),
                ('image_name', models.ImageField(upload_to=funcs.FileUpload.upload_to, verbose_name='image of group')),
                ('slug', models.CharField(max_length=100, verbose_name='slug url')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Confirm time!')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('is_active', models.BooleanField(default=True, verbose_name='status of brand')),
                ('group_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Parent_of_product', to='product.groupproduct', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.AddField(
            model_name='feature',
            name='product_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_of_feature', to='product.groupproduct', verbose_name='group feature'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Product name')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='description')),
                ('image_name', models.ImageField(upload_to=funcs.FileUpload.upload_to, verbose_name='image of product')),
                ('price_buy', models.PositiveIntegerField(default=0, verbose_name='buy price')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('is_active', models.BooleanField(default=True, verbose_name='status')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Confirm time!')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('slug', models.CharField(blank=True, max_length=30, null=True, verbose_name='اسلاگ')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='product.brand')),
                ('product_group', models.ManyToManyField(related_name='product_of_groups', to='product.groupproduct', verbose_name='group product')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40, verbose_name='value feature')),
                ('english', models.CharField(blank=True, max_length=20, null=True, verbose_name='english')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_product', to='product.feature', verbose_name='feature')),
                ('filter_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.featurevalue', verbose_name='filtring value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features_value', to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Product Feature',
                'verbose_name_plural': 'Product Featues',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(through='product.ProductFeature', to='product.feature'),
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.ImageField(upload_to=funcs.FileUpload.upload_to, verbose_name='images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Gallery', to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
