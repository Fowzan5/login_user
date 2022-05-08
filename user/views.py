from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer, Userserializer
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
import math, random
from django.core.mail import send_mail
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

    @action(detail=False, methods=['post'])
    def email_otp(self, request):
        if self.request.query_params.get("email") != "0":
            email = self.request.query_params.get("email")
            print(email)
            digits = "0123456789"
            otp = ""
            for i in range(4) :
                otp += digits[math.floor(random.random() * 10)]
            
            
            send_mail(
                'OTP',
                'The otp fot this email is:'+otp,
                'mohamedfowzanp@gmail.com',
                [email],
                fail_silently=False,
            )
            User.objects.filter(email=email).update(password=make_password(otp))
            # usr.set_password(otp)
            # return otp
        return Response({'key': 'value'})