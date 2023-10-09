from rest_framework.permissions import BasePermission

from users.models import User

user = User()


class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        return not user.groups.filter(name='Moderator')


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().owner

