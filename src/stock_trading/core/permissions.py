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
