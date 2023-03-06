from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Tip_Trick
from .serializers import Tip_TrickSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_tip_trick(request):
    tip_trick = Tip_Trick.objects.all()
    serializer = Tip_TrickSerializer(tip_trick, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def user_tip_trick(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = Tip_TrickSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        tip_trick = Tip_Trick.objects.filter(user_id=request.user.id)
        serializer = Tip_TrickSerializer(tip_trick, many=True)
        return Response(serializer.data)