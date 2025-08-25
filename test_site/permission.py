from rest_framework import permissions

class CheckRole(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.students == request.user


class CheckRoleReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'teachers':
            return False
        return True