from django.urls import path
from . import views

urlpatterns = [
    path('artist', views.artists_list),
    path('artist/new', views.new_artist),
    path('artist/<int:id>', views.get_artist),
    path('artist/put/<int:id>', views.edit_artist),
    path('artist/del/<int:id>', views.delete_artist),
    path('album', views.album_list),
    path('album/new', views.new_album),
    path('album/<int:id>', views.get_album),
    path('album/put/<int:id>', views.edit_album),
    path('album/del/<int:id>', views.delete_album),
    path('song', views.songs_list),
    path('song/new', views.new_song),
    path('song/<int:id>', views.get_song),
    path('song/put/<int:id>', views.edit_song),
    path('song/del/<int:id>', views.delete_song),
    path('songs', views.get_songs),
]
