from rest_framework.permissions import BasePermission

from course.models import Subscriber
from users.models import User, UserRole

user = User()


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        return False


class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        return not user.groups.filter(name='Moderator')


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        if Subscriber.is_subscribed:
            return True
