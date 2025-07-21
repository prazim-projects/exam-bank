from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import *
from fetenaArchive.models import User, Exam

# Create your views here.



class UploadExamView(APIView):
    serializer_class = ExamUploadSerializer

    def post(self, request):
         #assume user is authenticate
         request.user  = User.objects.first()