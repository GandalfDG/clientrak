from rest_framework import generics

from clients.models import Agent, Trip
from clients.serializers import TripSerializer

# Create your views here.
class AgentTrips(generics.ListCreateAPIView):
    def get_serializer_class(self):
        return TripSerializer

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)


    # def get_queryset(self):
    #     return Trip.objects.all()

    def get_queryset(self):
        agent = Agent.objects.get(user__username=self.request.user.get_username())
        agent_trips = Trip.objects.filter(client__agent__user__username=agent.user.get_username())
        return agent_trips