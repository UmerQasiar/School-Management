from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    Allows access only to users with role = 'admin'
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'admin'
