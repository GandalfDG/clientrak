from rest_framework.permissions import BasePermission

from clients.models import Agent, Trip

class UserTripPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        agent = Agent.objects.get(user__username=request.user.get_username())
        return obj.client.agent == agent
