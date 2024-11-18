from django.urls import path
from .views import (
    ProuductListGeneric,
    ProductDetailGeneric,
    BrandistGeneric,
    BrandDetailGeneric,
    GroupProductGeneric,
    GroupProductDetail,
    FeatureGeneric,
    FeatureDetailGeneric,
    FeatureValueGeneric,
    ProductFeatureGeneric,
    ProductFeatureGenericDetail,
    ProdudctGalleyGeneric,
    ProductGalleryGenericDetail,
    Cheapest_product,
    recently_product,
    Related_product,
    Related_product_group,
    RelatedGroupsOfGroup,
    FeatureGroup
)

urlpatterns = [
    # Product URLs
    path('products/', ProuductListGeneric.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailGeneric.as_view(), name='product-detail'),

    # Brand URLs
    path('brands/', BrandistGeneric.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailGeneric.as_view(), name='brand-detail'),

    # Group Product URLs
    path('group-products/', GroupProductGeneric.as_view(), name='group-product-list'),
    path('group-products/<int:pk>/', GroupProductDetail.as_view(), name='group-product-detail'),

    # Feature URLs
    path('features/', FeatureGeneric.as_view(), name='feature-list'),
    path('features/<int:pk>/', FeatureDetailGeneric.as_view(), name='feature-detail'),

    # Feature Value URLs
    path('feature-values/', FeatureValueGeneric.as_view(), name='feature-value-list'),

    # Product Feature URLs
    path('product-features/', ProductFeatureGeneric.as_view(), name='product-feature-list'),
    path('product-features/<int:pk>/', ProductFeatureGenericDetail.as_view(), name='product-feature-detail'),

    # Product Gallery URLs
    path('product-galleries/', ProdudctGalleyGeneric.as_view(), name='product-gallery-list'),
    path('product-galleries/<int:pk>/', ProductGalleryGenericDetail.as_view(), name='product-gallery-detail'),

    path('cheapest_product/',Cheapest_product.as_view()),
    path('recently_product/',recently_product.as_view()),

    path('related_product/<str:slug>/',Related_product.as_view()),
    path('related_product_group/<str:slug>/',Related_product_group.as_view()),

    path('related_group_group/<str:slug>/',RelatedGroupsOfGroup.as_view()),
    path('FeatureGroup/<str:slug>/',FeatureGroup.as_view()),
]
