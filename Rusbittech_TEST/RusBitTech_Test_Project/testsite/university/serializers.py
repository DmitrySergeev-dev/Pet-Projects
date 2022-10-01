from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *

#на низком уровне
class StudentSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.save()
        return instance


class TeacherSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    academic_degree = serializers.CharField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.academic_degree = validated_data.get("academic_degree", instance.academic_degree)
        instance.save()
        return instance

# с помощью класса ModelSerializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsGroup
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
# для теста
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
# def encode():
#     model = WomenModel('Angelina Djoli', 'The best women')
#     print(model)
#     model_ser = WomenSerializer(model)
#     print(model_ser.data, type(model_ser.data), sep='\n')
#     json = JSONRenderer().render(model_ser.data)
#     print(json)
