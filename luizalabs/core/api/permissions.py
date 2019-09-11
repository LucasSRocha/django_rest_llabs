from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Classe de permissão para visualização e alteração de objetos com property owner.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user or request.user.is_staff


class IsUserOrAdmin(permissions.BasePermission):
    """
    Classe de permissão para modificação de objeto caso o usuário seja staff ou
    o próprio usuário.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.pk == request.user.pk
