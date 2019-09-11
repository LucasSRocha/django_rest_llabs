from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.models import Product
from core.models import WishList
from core.models import UserMagalu

from .serializers import ProductSerializer
from .serializers import WishListSerializer
from .serializers import UserMagaluSerializer
from .serializers import UserMagaluSerializerReadOnly

from .permissions import IsOwnerOrAdminOrReadOnly
from .permissions import IsUserOrAdmin

from .utils import collect_wishlist
from .utils import check_product_existence


class UserMagaluAPIView(viewsets.ViewSet):

    queryset = UserMagalu.objects.all()

    serializer_class = UserMagaluSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]

        else:
            permission_classes = [IsUserOrAdmin]

        return [permission() for permission in permission_classes]

    def list(self, request):

        user = UserMagalu.objects.all()

        serializer = UserMagaluSerializerReadOnly(user, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):

        serializer = UserMagaluSerializer(data=request.data)

        if serializer.is_valid():
            user = UserMagalu.objects.create_user(username=serializer.validated_data.get('username'),
                                                  email=serializer.validated_data.get('email'))

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response({f'O email {request.data.get("email")} já está em uso!'}, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):

        try:
            user = UserMagalu.objects.get(pk=pk)

            serializer = UserMagaluSerializer(user)

            return Response(serializer.data, status.HTTP_200_OK)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        try:
            user = UserMagalu.objects.get(pk=pk)

            serializer = UserMagaluSerializer(user, data=request.data)

            if serializer.is_valid():
                user.email = serializer.validated_data.get('email')

                user.username = serializer.validated_data.get('username')

                user.set_password(user.username)

                user.save()

                return Response(serializer.data, status.HTTP_200_OK)

            return Response({f'O email {request.data.get("email")} já está em uso!'}, status.HTTP_403_FORBIDDEN)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        try:
            user = UserMagalu.objects.get(pk=pk)

            user.delete()

            return Response({'Usuário Deletado'}, status.HTTP_200_OK)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)


class WishListAPIView(viewsets.ViewSet):

    queryset = WishList.objects.all()

    serializer_class = WishListSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]

        else:
            permission_classes = [IsOwnerOrAdminOrReadOnly]

        return [permission() for permission in permission_classes]

    def list(self, request):

        wishlist = WishList.objects.all()

        serializer = WishListSerializer(wishlist, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):

        serializer = WishListSerializer(data=request.data)

        if serializer.is_valid():

            WishList.objects.create_user(wishlist_name=serializer.validated_data.get('wishlist_name'),
                                         magalu_user=serializer.validated_data.get('magalu_user'))

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response({f'O Usuário já possui uma lista de favoritos!'}, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):

        try:
            products = [p.product_id for p in Product.objects.filter(wishlist__pk=pk)]

            return Response({"WishList": collect_wishlist(products)}, status.HTTP_200_OK)

        except WishList.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        try:
            wishlist = WishList.objects.get(pk=pk)

            serializer = WishListSerializer(wishlist, data=request.data)

            if serializer.is_valid():
                wishlist.wishlist_name = serializer.validated_data.get('wishlist_name')

                wishlist.save()

                return Response(serializer.data, status.HTTP_200_OK)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        try:
            wishlist = WishList.objects.get(pk=pk)

            wishlist.delete()

            return Response({'WishList Deletada'}, status.HTTP_200_OK)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)


class ProductAPIView(viewsets.ViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticatedOrReadOnly]

        else:
            permission_classes = [IsOwnerOrAdminOrReadOnly]

        return [permission() for permission in permission_classes]

    def list(self, request):

        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):

        if check_product_existence(request.data.get('product_id')):

            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():

                Product.objects.create(wishlist=serializer.validated_data.get('wishlist'),
                                       product_name=serializer.validated_data.get('product_name'),
                                       product_id=serializer.validated_data.get('product_id'))

                return Response(serializer.data, status.HTTP_201_CREATED)

            return Response({'Produto já existe na WishList'}, status.HTTP_403_FORBIDDEN)

        return Response({'O Produto não existe'}, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):

        try:
            product = Product.objects.get(pk=pk)

            serializer = ProductSerializer(product)

            return Response(serializer.data, status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):

        try:
            product = Product.objects.get(pk=pk)

            serializer = ProductSerializer(product, data=request.data)

            if serializer.is_valid():
                product.product_name = serializer.validated_data.get('product_name')

                product.product_id = serializer.validated_data.get('product_id')

                product.save()

                return Response(serializer.data, status.HTTP_200_OK)

        except UserMagalu.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):

        try:
            product = Product.objects.get(pk=pk)

            product.delete()

            return Response({'Produto Deletada'}, status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response({'Object does not exists.'}, status.HTTP_404_NOT_FOUND)
