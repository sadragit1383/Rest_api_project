from rest_framework import serializers

from .models import Product,Brand,GroupProduct,Feature,FeatureValue,ProductGallery,ProductFeature

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'



class GroupProductSerilazer(serializers.ModelSerializer):

    class Meta:
        model = GroupProduct
        fields = '__all__'


class FeatureSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = '__all__'




class FeatureValueSerilizer(serializers.ModelSerializer):

    class Meta:
        model = FeatureValue
        fields = '__all__'



class ProductFeatureSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ProductFeature
        fields = '__all__'



class ProductGallerySerilizer(serializers.ModelSerializer):

    class Meta:
        model = ProductGallery
        fields = '__all__'

