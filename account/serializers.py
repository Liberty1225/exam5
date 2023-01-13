from rest_framework import serializers

from .models import Author,User


class RegisterAuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_2')

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        Author.objects.create(user=user)
        return user
