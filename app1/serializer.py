from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class Registerserailizer(serializers.Serializer):
    username=serializers.CharField(max_length=250)
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):

        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"password do not match"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user