from django.contrib.auth.models import User
from rest_framework import serializers
from LearnHub.models import CategoryDb,CourseDb,EnrollmentDb

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","email"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDb
        fields = "__all__"
        read_only_fields=["id","created_at","user"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDb
        fields = "__all__"
        read_only_fields = ["id","user","created_at","update_at"]


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentDb
        fields = "__all__"
        read_only_fields = ["student","enrolled_at"]
        