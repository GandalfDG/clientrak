from rest_framework.permissions import BasePermission

from clients.models import Agent, Trip

class UserTripPermission(BasePermission):

    """
    permission to access a particular Trip object is granted if the logged
    in user is the agent for the trip.
    """

    def has_object_permission(self, request, view, obj):
        agent = Agent.objects.get(user__username=request.user.get_username())
        return obj.client.agent == agent
