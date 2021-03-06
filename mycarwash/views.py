from django.shortcuts import render

# Create your views here.
from .models import (
    CarModel,
    SelectionServices,
    RequestUser,
    DeleteRequest,
    DiscountCode,
    Comment
)
from .serializers import (
    GetCarModelSerializer,
    GetSelectionServicesSerializer,
    PostDeleteRequest,
    PostDiscountCode,
    PostRequestUser,
    PostSatisfactionUser,
    PostDoIt,
    GetRequestUser,
    GetRequestUserForUpdate,
    GetRequestUsers

)
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from djoser import permissions
from rest_framework.views import APIView


class GetCarModel(APIView):
    def get(self, request):
        queryset = CarModel.objects.all()
        serializer_class = GetCarModelSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class GetSelectionServices(generics.ListAPIView):
    serializer_class = GetSelectionServicesSerializer
    queryset = SelectionServices.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["name_car"]


class PostDetailUser(generics.ListCreateAPIView):
    serializer_class = PostRequestUser
    queryset = RequestUser.objects.all()


class GetSatisfactionUser(generics.ListAPIView):
    serializer_class = PostSatisfactionUser
    queryset = Comment.objects.all()


class PutSatisfactionUser(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = PostSatisfactionUser


class GetRequestUser(generics.ListAPIView):
    queryset = RequestUser.objects.all()
    serializer_class = GetRequestUser
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["doit"]


class GetRequestUserForUser(generics.ListAPIView):
    queryset = RequestUser.objects.all()
    serializer_class = GetRequestUsers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["author"]


class DeleteRequestUser(APIView):
    def delete(self, request, pk):
        queryset = RequestUser.objects.get(pk=pk)
        serializer_class = PostRequestUser
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteReasonUser(generics.ListCreateAPIView):
    queryset = DeleteRequest.objects.all()
    serializer_class = PostDeleteRequest


class CreateCode(generics.ListCreateAPIView):
    queryset = DiscountCode.objects.all()
    serializer_class = PostDiscountCode


class PutCode(APIView):
    def put(self, request, pk):
        queryset = DiscountCode.objects.get(pk=pk)
        serializer_class = PostDiscountCode(
            queryset, data=request.data, context={'request': request})
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.error, status=status.HTTP_400_BAD_REQUEST)


class GetUserCode(generics.ListAPIView):
    queryset = DiscountCode.objects.all()
    serializer_class = PostDiscountCode
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["user"]


class GetUserCodeForAdmin(generics.ListAPIView):
    queryset = DiscountCode.objects.all()
    serializer_class = PostDiscountCode


class GetDeleteReasonUser(generics.ListAPIView):
    queryset = DeleteRequest.objects.all()
    serializer_class = PostDeleteRequest
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["count"]


class PutRequestUserForAdmin(APIView):

    def put(self, request, pk):
        queryset = RequestUser.objects.get(pk=pk)
        serializer_class = GetRequestUserForUpdate(
            queryset, data=request.data, context={'request': request})
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.error, status=status.HTTP_400_BAD_REQUEST)
