from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Diver
from .serializers import DiverSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_divers(request):
    divers = Diver.objects.all()
    serializer = DiverSerializer(divers, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_divers(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = DiverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        divers = Diver.objects.all()
        serializer = DiverSerializer(divers, many=True)
        return Response(serializer.data)
    
@api_view(['PATCH'])
@permission_classes([AllowAny])
def available(request, user_id):
        # print(
        # 'User ', f"{request.user.id} {request.user.email} {request.user.username}")   
        diver = get_object_or_404(Diver, user_id=user_id)  
        serializer = DiverSerializer(diver, {'user_availibility':True}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([AllowAny])
def unavailable(request, user_id):
        print(request)     
        diver = get_object_or_404(Diver, user_id=user_id)  
        serializer = DiverSerializer(diver, {'user_availibility':False}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
     

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_by_id(request,user_id):
    divers = Diver.objects.filter(user_id=user_id)
    serializer = DiverSerializer(divers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_by_city(request,user_city):
    divers = Diver.objects.filter(user_city=user_city)
    serializer = DiverSerializer(divers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_by_state(request,user_state):
    divers = Diver.objects.filter(user_state=user_state)
    serializer = DiverSerializer(divers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_by_country(request,user_country):
    divers = Diver.objects.filter(user_country=user_country)
    serializer = DiverSerializer(divers, many=True)
    return Response(serializer.data)

