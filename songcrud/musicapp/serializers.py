from rest_framework import serializers
from .models import Lyric, Song

class LyricsSerializer(serializers.ModelSerializer):
     class Meta:
         model = Lyric
         fields = ['content']


class SongSerializer(serializers.ModelSerializer):
    #to get lyrics content in song
     lyrics = serializers.SerializerMethodField('get_lyrics')
     artist_id = serializers.StringRelatedField(read_only=True)

     def get_lyrics(self, instance):
         query = instance.lyric_set.all()
         lyrics = LyricsSerializer(query, many=True).data
         return lyrics

     class Meta:
        model = Song
        fields = ['id', 'artist_id', 'title', 'date_released','likes', 'lyrics' ]

class UpdateSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['title', 'date_released', 'artist_id']