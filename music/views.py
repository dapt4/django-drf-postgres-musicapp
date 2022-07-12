from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artist, Album, Song
from rest_framework import status
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, ArtistSerializer2, AlbumSerializer2, AlbumSerializer3

# Create your views here.

@api_view(['GET'])
def artists_list(request):
    try:
        artists = Artist.objects.all()
        for artist in artists:
            albums = artist.albums.all()
            artist.albums.set(albums)
            list_songs = []
            for album in albums:
                songs = album.songs.all()
                for song in songs:
                    list_songs.append(song)
            artist.songs = list_songs
        if artists:
            serializer = ArtistSerializer2(artists, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
        albums = artist.albums.all()
        artist.albums.set(albums)
        list_songs = []
        for album in albums:
            songs = album.songs.all()
            for song in songs:
                list_songs.append(song)
        artist.songs = list_songs
        print({"art": artist.songs})
        if artist:
            serializer = ArtistSerializer2(artist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def new_artist(request):
    try:
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def edit_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_artist(request, id):
    try:
        artist = Artist.objects.get(id=id)
        if artist:
            artist.delete()
            serializer = ArtistSerializer(artist)
            return Response(serializer.data)
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def album_list(request):
    try:
        albums = Album.objects.all()
        if albums:
            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def new_album(request):
    try:
        artist = Artist.objects.get(id=request.data['artist'])
        album = Album(
            title=request.data['title'],
            description=request.data['description'],
            year=request.data['year'],
            artist=artist
        )
        album.save()
        serializer = AlbumSerializer(album)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_album(request, id):
    try:
        album = Album.objects.get(id=id)
        songs = album.songs.all()
        album.songs.set(songs)
        serializer = AlbumSerializer2(album)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def edit_album(request, id):
    try:
        album = Album.objects.get(id=id)
        artist = Artist.objects.get(id=request.data['artist'])
        album.title = request.data['title']
        album.description = request.data['description']
        album.year = request.data['year']
        album.artist = artist
        album.save()
        serializer = AlbumSerializer(album)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_album(request, id):
    try:
        album = Album.objects.get(id=id)
        if album:
            album.delete()
            serializer = AlbumSerializer(album)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def songs_list(request):
    try:
        songs = Song.objects.all()
        if songs:
            serializer = SongSerializer(songs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def new_song(request):
    try:
        album_id = request.data['album']
        album = Album.objects.get(id=album_id)
        song = Song(
            title = request.data['title'],
            duration = request.data['duration'],
            album = album
        )
        song.save()
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_song(request, id):
    try:
        song = Song.objects.get(id=id)
        if song:
            serializer = SongSerializer(song)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as err:
        print(err)
        return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def edit_song(request, id):
    try:
        album_id = request.data['album']
        album = Album.objects.get(id=album_id)
        song = Song.objects.get(id=id)
        song.title = request.data['title']
        song.duration = request.data['duration']
        song.album = album
        song.save()
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_song(request, id):
    try:
        song = Song.objects.get(id=id)
        if song:
            song.delete()
            serializer = SongSerializer(song)
            return Response(serializer.data)
        return Response({"error":"not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        print(err)
        return Response({"error":"internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_songs(request):
    albums = Album.objects.prefetch_related("songs").all()
    serializer = AlbumSerializer3(albums, many=True)
    return Response(serializer.data)

