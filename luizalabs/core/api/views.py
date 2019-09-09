from django.db.models import Q

from rest_framework import mixins
from rest_framework import generics

from core.models import UserMagalu
from .permissions import IsOwnerOrReadOnly
from .serializers import UserMagaluSerializer


class UserMagaluAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = UserMagaluSerializer

    def get_queryset(self):
        query_set = UserMagalu.objects.all()
        query_string = self.request.GET.get("q")
        if query_string is not None:
            query_set = query_set.filter(
                    Q(title__icontains=query_string)|
                    Q(content__icontains=query_string)
                    ).distinct()
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserMagaluRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_fields = 'pk'  # slug, id # url(r'?P<pk>\d+')
    serializer_classs = UserMagaluSerializer
    permission_classess = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return UserMagalu.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
