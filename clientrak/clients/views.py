from rest_framework import generics

from clients.models import Agent, Trip
from clients.serializers import TripSerializer
from clients.permissions import UserTripPermission

# Create your views here.
class AgentTrips(generics.ListCreateAPIView):

    lookup_field = 'id'

    def get_serializer_class(self):
        return TripSerializer

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        agent = Agent.objects.get(user__username=self.request.user.get_username())
        agent_trips = Trip.objects.filter(client__agent__user__username=agent.user.get_username())
        return agent_trips

class UpdateTrip(generics.RetrieveUpdateAPIView):

    permission_classes = [UserTripPermission]
    serializer_class = TripSerializer

    def get_queryset(self):
        agent = Agent.objects.get(user__username=self.request.user.get_username())
        agent_trips = Trip.objects.filter(client__agent=agent)
        return agent_trips
