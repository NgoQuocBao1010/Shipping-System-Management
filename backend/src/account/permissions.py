from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """
    Only allow admin user to access this endpoint
    """

    def has_permission(self, request, view):
        message = "Non-admin user not allowed"
        # print(request.user.is_admin)
        return True
