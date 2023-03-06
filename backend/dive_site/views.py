from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Dive_Site
from .serializers import DiveSiteSerializer
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_dive_sites(request):
    cars = Dive_Site.objects.all()
    serializer = DiveSiteSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_dive_sites(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = DiveSiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        dive_sites = Dive_Site.objects.all()
        serializer = DiveSiteSerializer(dive_sites, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_by_id(request, id):
    dive_site = Dive_Site.objects.filter(id=id)
    serializer = DiveSiteSerializer(dive_site, many=True)
    return Response(serializer.data)