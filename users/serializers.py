from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Profile
from django.contrib.auth.models import User


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password",
                  "first_name", "last_name", "profile")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        profile_data = validated_data.pop("profile")

        # create profile
        print(user)
        Profile.objects.create(
            user=user,
            title=profile_data["title"],
            headline=profile_data["headline"],
        )

        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
