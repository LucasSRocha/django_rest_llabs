from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from core.models import Product
from core.models import WishList
from core.models import UserMagalu

from .serializers import ProductSerializer
from .serializers import WishListSerializer
from .serializers import UserMagaluSerializer
from .serializers import UserMagaluSerializerReadOnly

from .permissions import IsOwnerOrReadOnly
from .permissions import IsUser


class UserMagaluAPIView(viewsets.ViewSet):
    queryset = UserMagalu.objects.all()
    serializer_class = UserMagaluSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsUser]
        return [permission() for permission in permission_classes]

    def list(self, request):
        user = UserMagalu.objects.all()

        serializer = UserMagaluSerializerReadOnly(user, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = UserMagalu.objects.get(pk=pk)

            serializer = UserMagaluSerializer(user)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'})

        return Response(request.user.pk == user.pk)

        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class WishListAPIView(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
            if self.action == 'list':
                permission_classes = [IsAuthenticatedOrReadOnly]
            else:
                permission_classes = [IsOwner]
            return [permission() for permission in permission_classes]

    def list(self, request):
        return Response('oi')

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
