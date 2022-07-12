from .models import Artist, Album, Song
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Album
        fields = ['id', 'title', 'description', 'year', 'artist']

class SongSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album']


class ArtistSerializer2(serializers.HyperlinkedModelSerializer):
    albums = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    songs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Artist
        fields = ['id', 'name', 'albums', 'songs']

class AlbumSerializer2(serializers.HyperlinkedModelSerializer):
    artist = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    songs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Album
        fields = ['id', 'title', 'description', 'year', 'artist', 'songs']

class AlbumSerializer3(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Album
        fields = ["id", "title", "description", "songs"]
