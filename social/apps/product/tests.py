import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Product, Brand, GroupProduct, Feature


@pytest.fixture
def api_client():
    """
    Returns an instance of APIClient for testing.
    """
    return APIClient()


@pytest.fixture
def sample_product():
    """
    Create a sample product for testing.
    """
    return Product.objects.create(name="Test Product", price=100.0)


@pytest.fixture
def sample_brand():
    """
    Create a sample brand for testing.
    """
    return Brand.objects.create(name="Test Brand")


@pytest.fixture
def sample_group_product():
    """
    Create a sample group product for testing.
    """
    return GroupProduct.objects.create(name="Test Group")


@pytest.mark.django_db
def test_product_list(api_client, sample_product):
    """
    Test the product list endpoint.
    """
    url = reverse("product-list")  # Update this with the correct name of your URL
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["name"] == sample_product.name


@pytest.mark.django_db
def test_product_detail(api_client, sample_product):
    """
    Test retrieving a product detail.
    """
    url = reverse("product-detail", args=[sample_product.id])  # Update with your URL name
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json()["name"] == sample_product.name


@pytest.mark.django_db
def test_product_creation(api_client):
    """
    Test creating a new product.
    """
    url = reverse("product-list")  # Update with your URL name
    payload = {"name": "New Product", "price": 200.0}

    response = api_client.post(url, payload)

    assert response.status_code == 201
    assert response.json()["name"] == "New Product"


@pytest.mark.django_db
def test_brand_list(api_client, sample_brand):
    """
    Test the brand list endpoint.
    """
    url = reverse("brand-list")  # Update with the correct URL name
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["name"] == sample_brand.name


@pytest.mark.django_db
def test_group_product_creation(api_client):
    """
    Test creating a new group product.
    """
    url = reverse("group-product-list")  # Update with the correct URL name
    payload = {"name": "New Group Product"}

    response = api_client.post(url, payload)

    assert response.status_code == 201
    assert response.json()["name"] == "New Group Product"
