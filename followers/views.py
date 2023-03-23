from rest_framework import generics, permissions
from drf_api.permissions import isOwnerOrReadOnly
from .models import Followers
from .serializers import FollowersSerializer


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [isOwnerOrReadOnly]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()
