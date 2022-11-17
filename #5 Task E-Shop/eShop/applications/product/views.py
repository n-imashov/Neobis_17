from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination

from .models import Product
from applications.product.serializers import ProductSerializer


class ProductPriceFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price',
                                            lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price',
                                            lookup_expr='lte')

    class Meta:
        model = Product
        fields = [
            'min_price',
            'max_price',
            'category',
        ]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ProductPriceFilter
    # filterset_fields = ['category', 'price', ]
    search_fields = ['title', 'description', ]


    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

