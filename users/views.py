from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import CustomUser, HR
from users.serializers import UserRegisterSerializer, HRRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class HRRegisterView(generics.CreateAPIView):
    queryset = HR.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = HRRegisterSerializer
