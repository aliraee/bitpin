from rest_framework import serializers
from .models import Post, Score


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['author', 'title', 'createdAt', 'meadPostScore', 'countOfUsers']
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class ScoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['user', 'post', 'value']
