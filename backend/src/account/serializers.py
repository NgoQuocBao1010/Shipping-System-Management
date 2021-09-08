from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ("user", "id", "dateCreated")

    def get_email(self, obj):
        return obj.user.email

    # def update(self, instance, validated_data):
    #     instance.fullName = self.validated_data.get('fullName', instance.fullName)
    #     instance.phone = self.validated_data.get('phone', instance.phone)
    #     instance.address = self.validated_data.get('address', instance.address)
    #     instance.gender = self.validated_data.get('gender', instance.gender)
    #     instance.dateOfBirth = self.validated_data.get('dateOfBirth', instance.dateOfBirth)

    #     instance.save()

    #     return instance
