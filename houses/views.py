from houses.models import House
from houses.serializers import HouseSerializer
from houses.permissions import IsOwnerOrReadOnly

from users.models import User

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions


class HouseList(generics.ListCreateAPIView):
    serializer_class = HouseSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        """
        Need login to POST
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Search by zipcode, address and username
        """
        queryset = House.objects.all()
        userid = self.request.GET.get('userid', None)
        username = self.request.GET.get('username', None)
        zipcode = self.request.GET.get('zipcode', None)
        address = self.request.GET.get('address', None)

        if userid is not None:
            queryset = queryset.filter(owner=userid)
        if userid is None and username is not None:
            # when userid doesn't exist, use username
            userid = User.objects.get(username=username)
            queryset = queryset.filter(owner=userid)
        if zipcode is not None:
            queryset = queryset.filter(zipcode=zipcode)
        if address is not None:
            queryset = queryset.filter(address__contains=address)
            # use contain filter for address searching

        return queryset



class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    For each house info:
        - PUT is allowed for owner only (need to login)
        - GET is allowed for every one (no need to login)
    """
    serializer_class = HouseSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_queryset(self):
        return House.objects.all()
