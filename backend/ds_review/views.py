from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import DS_Review
from .serializers import DS_ReviewSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_ds_review(request):
    ds_review = DS_Review.objects.all()
    serializer = DS_ReviewSerializer(ds_review, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_ds_review(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = DS_ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        ds_review = DS_Review.objects.filter(user_id=request.user.id)
        serializer = DS_ReviewSerializer(ds_review, many=True)
        return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_ds_post_review (request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = DS_ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_review_by_site_name(request, site_name):
    ds_review = DS_Review.objects.filter(site_name=site_name)
    serializer = DS_ReviewSerializer(ds_review, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_review_by_site_id(request, dive_site_id):
    ds_review = DS_Review.objects.filter(dive_site_id=dive_site_id)
    serializer = DS_ReviewSerializer(ds_review, many=True)
    return Response(serializer.data)