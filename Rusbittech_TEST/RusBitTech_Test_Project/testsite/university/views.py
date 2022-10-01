from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.
#на низком уровне
class StudentAPIView(APIView):
    def get(self, request):
        s = Student.objects.all()
        return Response({'info': StudentSerializer(s, many=True).data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # автоматически вызовет метод create() из сериализатора
        return Response({'info_about_student': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Student.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesn't exist"})
        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'changed_info': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            record = Student.objects.get(pk=pk)  # находим нужную запись в БД
        except:
            return Response({"error": "Object doesn't exist"})
        record.delete()
        return Response({"info": "delete student" + str(pk)})


class TeacherAPIView(APIView):
    def get(self, request):
        t = Teacher.objects.all()
        return Response({'info': TeacherSerializer(t, many=True).data})

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # post_new = Teacher.objects.create(
        #     full_name=request.data['full_name'],
        #     academic_degree=request.data['academic_degree'],
        # )
        # return Response({'teacher': TeacherSerializer(post_new).data})

        serializer.save()  # автоматически вызовет метод create() из сериализатора
        return Response({'info_about_teacher': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Teacher.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesn't exist"})
        serializer = TeacherSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'changed_info': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            record = Teacher.objects.get(pk=pk)  # находим нужную запись в БД
        except:
            return Response({"error": "Object doesn't exist"})
        record.delete()
        return Response({"info": "delete teacher" + str(pk)})

#с помощью класса ListCreateAPIView
class SubjectAPIList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class StudentsGroupAPIList(generics.ListCreateAPIView):
    queryset = StudentsGroup.objects.all()
    serializer_class = StudentsGroupSerializer

class LessonAPIList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
