from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile,Job,Application

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['skills', 'experience']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)

        if profile_data:
            Profile.objects.create(user=user, **profile_data)

        return user


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'salary', 'employer', 'created_at']
        read_only_fields = ['employer', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Job.objects.create(employer=user, **validated_data)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'user', 'job', 'applied_at']
        read_only_fields = ['user', 'applied_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Application.objects.create(user=user, **validated_data)
