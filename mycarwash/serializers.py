from rest_framework import serializers
from .models import (
    CarModel,
    SelectionServices,
    RequestUser,
    DeleteRequest,
    DiscountCode,
    Comment
)


class GetCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('name_car', 'image')


class GetSelectionServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionServices
        fields = ('name_car', 'discription', 'discription_pack', 'price')


class PostDeleteRequest(serializers.ModelSerializer):
    class Meta:
        model = DeleteRequest
        fields = ('author', 'discription_service', 'count')


class PostDiscountCode(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = ('id', 'user', 'code', 'counter', 'orders')


class PostRequestUser(serializers.ModelSerializer):
    class Meta:
        model = RequestUser
        fields = ('author', 'name_car', 'discription_service',
                  'price', 'lat', 'lng', 'timedate', 'model', 'color', 'car_tag', 'payment_type', 'doit')


class GetRequestUser(serializers.ModelSerializer):
    class Meta:
        model = RequestUser
        fields = ('id', 'author', 'name_car', 'discription_service',
                  'price', 'lat', 'lng', 'timedate', 'model', 'color', 'car_tag', 'payment_type', 'doit')


class GetRequestUsers(serializers.ModelSerializer):
    class Meta:
        model = RequestUser
        fields = ('id', 'author', 'price', 'timedate', 'doit')


class GetRequestUserForUpdate(serializers.ModelSerializer):
    class Meta:
        model = RequestUser
        fields = ('id', 'doit')


class PostSatisfactionUser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'satisfaction')


class PostDoIt(serializers.ModelSerializer):
    class Meta:
        model = RequestUser
        fields = ('id', 'author', 'doit')
