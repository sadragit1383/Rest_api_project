"""
Views for handling product-related APIs in the project.
Includes CRUD operations for products, brands, groups, features, and galleries.
"""

from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.db.models import Q, Count

from .models import (
    Product,
    Brand,
    ProductGallery,
    ProductFeature,
    Feature,
    GroupProduct,
    FeatureValue
)
from .serializers import (
    ProductGallerySerializer,
    ProductFeatureSerializer,
    FeatureSerializer,
    ProductSerializer,
    BrandSerializer,
    GroupProductSerializer
)

# Generic Views for CRUD Operations
class ProductListGeneric(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandListGeneric(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class GroupProductGeneric(generics.ListCreateAPIView):
    queryset = GroupProduct.objects.all()
    serializer_class = GroupProductSerializer


class GroupProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupProduct.objects.all()
    serializer_class = GroupProductSerializer


class FeatureGeneric(generics.ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureValueGeneric(generics.ListCreateAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureSerializer


class ProductFeatureGeneric(generics.ListCreateAPIView):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer


class ProductFeatureDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer


class ProductGalleryGeneric(generics.ListCreateAPIView):
    queryset = ProductGallery.objects.all()
    serializer_class = ProductGallerySerializer


class ProductGalleryDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductGallery.objects.all()
    serializer_class = ProductGallerySerializer

# Custom Views
class CheapestProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('price')[:1]  # Get the cheapest product


class RecentlyAddedProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-register_date')  # Most recent first


class RelatedProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        product = Product.objects.filter(slug=slug).first()
        if not product:
            return Product.objects.none()

        related_groups = product.product_group.all()
        return Product.objects.filter(
            is_active=True,
            product_group__in=related_groups
        ).exclude(id=product.id).distinct()


class RelatedProductGroup(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        group = get_object_or_404(GroupProduct, slug=slug)
        return Product.objects.filter(is_active=True, product_group=group)


class RelatedGroupsOfGroup(generics.ListAPIView):
    serializer_class = GroupProductSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        group = get_object_or_404(GroupProduct, slug=slug)
        return GroupProduct.objects.filter(
            is_active=True,
            group_parent=group.id
        )


class FeatureGroup(generics.ListCreateAPIView):
    serializer_class = FeatureSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        group = get_object_or_404(GroupProduct, slug=slug)
        return Feature.objects.filter(
            is_active=True,
            product_group=group
        )


class BrandGroup(generics.ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        group = get_object_or_404(GroupProduct, slug=slug)
        brand_ids = group.Parent.filter(is_active=True).values_list('brand_id', flat=True)
        return Brand.objects.filter(pk__in=brand_ids).annotate(
            count=Count('brands')
        ).filter(count__gt=0).order_by('-count')
