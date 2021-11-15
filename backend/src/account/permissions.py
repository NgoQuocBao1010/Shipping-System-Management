from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """
    Only allow admin user to access this endpoint
    """

    def has_permission(self, request, view):
        message = "Non-admin user not allowed"
        return request.user.is_admin


class StaffOnly(permissions.BasePermission):
    """
    Only allow staff user (driver and manager) to access this endpoint
    """

    def has_permission(self, request, view):
        message = "Non-staff user not allowed"
        return request.user.is_staff
