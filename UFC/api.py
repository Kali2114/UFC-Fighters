from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Fighter
from .serializers import UserSerializer, FighterSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FighterView(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer

