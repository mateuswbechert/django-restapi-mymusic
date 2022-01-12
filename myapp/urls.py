from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    re_path(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name='music-detail'),

    re_path(r'^albuns/$', views.AlbumList.as_view()),
    re_path(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),

    re_path(r'^bands/$', views.BandList.as_view()),
    re_path(r'^band/(?P<pk>[0-9]+)/$', views.BandDetail.as_view()),

    re_path(r'^members/$', views.MemberList.as_view()),
    re_path(r'^member/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
]