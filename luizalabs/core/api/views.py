from rest_framework import viewsets

from core.models import Product
from core.models import WishList
from core.models import UserMagalu

from .serializers import ProductSerializer
from .serializers import WishListSerializer
from .serializers import UserMagaluSerializer

from .permissions import IsOwnerOrReadOnly


class UserMagaluAPIView(viewsets.ModelViewSet):
    queryset = UserMagalu.objects.all()
    serializer_class = UserMagaluSerializer


class WishListAPIView(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
