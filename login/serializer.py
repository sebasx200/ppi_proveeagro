from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=False, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=False)
    current_password = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_superuser = serializers.BooleanField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "password2",
            "current_password",
            "is_superuser",
            "email",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        # Check if both password fields match
        if "password" in data and "password2" in data:
            if data["password"] != data["password2"]:
                raise serializers.ValidationError(
                    {"password": "Las contraseñas no coinciden"}
                )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user

    def update(self, instance, validated_data):
        # Check if the current password is provided and correct
        if "current_password" in validated_data:
            if not instance.check_password(validated_data["current_password"]):
                raise serializers.ValidationError(
                    {"current_password": "Current password is not correct"}
                )
            validated_data.pop("current_password")

        # If new password is provided, update it
        if "password" in validated_data and "password2" in validated_data:
            if validated_data["password"] != validated_data["password2"]:
                raise serializers.ValidationError(
                    {"password": "Las contraseñas no coinciden"}
                )
            instance.set_password(validated_data["password"])
            validated_data.pop("password")
            validated_data.pop("password2")

        # Update the rest of the fields
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()

        return instance
