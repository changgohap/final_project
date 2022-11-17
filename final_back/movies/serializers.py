from rest_framework import serializers
from .models import Actor, Movie, Genre, Review

# MovieList Page를 렌더링할 때 필요한 시리얼 라이저
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

# MovieDetail Page를 렌더링할 때 필요한 시리얼 라이저
class MovieSerializer(serializers.ModelSerializer):
    # 해당 무비를 좋아하는 사람의 숫자를 나타내고 싶다.
    movie_lovers_set = serializers.IntegerField(source='like_users.count', read_only=True)
     
    class Meta:
        model = Movie
        fields = '__all__'

# ActorList Page를 렌더링할 때 필요한 시리얼 라이저
class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'

# Actor Detail Page를 렌더링할 때 필요한 시리얼 라이저
class ActorSerializer(serializers.ModelSerializer):
    # 해당 배우를 좋아하는 사람의 숫자를 나타내고 싶다.
    actor_lovers_set = serializers.IntegerField(source='like_users.count', read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'

##############################################################
# Genre 활용할 때 필요한 시리얼 라이저
class GenreListSerializer(serializers.ModelSerializer):
    movies_in_genre = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies_in_genre',)
        depth = 1

class GenreSerializer(serializers.ModelSerializer):
    # 장르에 해당하는 모든 영화를 받기
    movies_in_genre = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Genre
        fields = '__all__'
        depth = 1

################################################################
class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'

#########################################################
class SimpleMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)


class ReviewSerializer(serializers.ModelSerializer):
    # 참조하고 있는 movie에서 정보를 가져오기
    movie = SimpleMovieSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ('movie', 'content', 'created_at', 'rank')
##########################################################
