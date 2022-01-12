from .models import Music, Album, Band, Member
from .serializers import MusicSerializer, AlbumSerializer, MemberSerializer, BandSerializer
from rest_framework import generics


class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class AlbumList(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class BandList(generics.ListCreateAPIView):

    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class MemberList(generics.ListCreateAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = MemberSerializer