from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
	Custom permission to only allow owners to edit an object.
	"""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or Options requsts.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission for owner
        return obj.owner == request.user
