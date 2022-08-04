from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from product.serializers import ProductSerializer

from .models import Product


class ProductViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer