from users.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        For non-superuser, only show login user
        """
        return User.objects.all().filter(username=self.request.user)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Dont allow users access other users
        by using filter(username=self.request.user).
        """
        return User.objects.all().filter(username=self.request.user)
