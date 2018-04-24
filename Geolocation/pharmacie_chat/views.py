from django.shortcuts import render
import geocoder
# Create your views here.
from geopy.distance import great_circle
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pharmacie_chat.models import donnee_pharmacie
from pharmacie_chat.serializers import DonneepharmacieSerializer
from pharmacie_chat.serializers import ProximiteSerializer

@csrf_exempt
def chatbot_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pharmacie = donnee_pharmacie.objects.all()
        serializer = DonneepharmacieSerializer(pharmacie, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DonneepharmacieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def pharmacie_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        pharmacie = donnee_pharmacie.objects.get(pk=pk)
    except donnee_pharmacie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DonneepharmacieSerializer(pharmacie)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DonneepharmacieSerializer(pharmacie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pharmacie.delete()
        return HttpResponse(status=204)

@csrf_exempt
def position_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        phar = donnee_pharmacie.objects.all()
        Query=[]
        for i in range(len(phar)): 
            Query.append(phar[i])

        #serializer = DonneepharmacieSerializer(phar, many=True)
        #pharmacie=serializer.data

        g = geocoder.ip('me')
        localise=(g.lat, g.lng)

        distance_position=[]
        for pharmacie in Query:
            lon_lat=(pharmacie.longitude, pharmacie.latitude)
            distance_position.append(great_circle(lon_lat, localise).miles)

        index_plus_proche=distance_position.index(min(distance_position))
        
        serializer = DonneepharmacieSerializer(Query[index_plus_proche])
        #return JsonResponse(serializer.data, safe=False)
        return HttpResponse(request.build_absolute_uri())

        
        
    

