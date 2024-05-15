# Stock Trading
# Created by Maximillian M. Estrada on 2024-05-15

from rest_framework import permissions


class UserReadOnly(permissions.BasePermission):
    """
    Allows safe methods access for non-admin users.
    """
    def has_permission(self, request, view):
        return bool(
            (request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated)
        )


class IsOwner(permissions.BasePermission):
    """
    Allows access only to the owner.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user'):
            return bool(request.user == obj.user and request.user and request.user.is_authenticated)
        return bool(request.user == obj.user and request.user and request.user.is_authenticated)
