from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from clients.models import Trip
from clients.serializers import TripSerializer

# Create your views here.
@csrf_exempt
def trip_list(request):
    if request.method == 'GET':
        trips =  Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return JsonResponse(serializer.data, safe=False)