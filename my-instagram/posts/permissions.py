from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user


class CanSeePost(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        following_user_list = request.user.folloing.filter(is_agree=True).values_list('to_user', flat=True)

        following_user_list = list(following_user_list) + [request.id]
        return obj.creator.is_public or obj.creator in following_user_list
