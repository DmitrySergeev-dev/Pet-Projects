"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from university.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/student/', StudentAPIView.as_view()),
    path('api/v1/student/<int:pk>/', StudentAPIView.as_view()),
    path('api/v1/teacher/', TeacherAPIView.as_view()),
    path('api/v1/teacher/<int:pk>/', TeacherAPIView.as_view()),
    path('api/v1/subject/', SubjectAPIList.as_view()),
    path('api/v1/studentsgroup/', StudentsGroupAPIList.as_view()),
    path('api/v1/lesson/', LessonAPIList.as_view()),
]
