from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Post, Score
from .serializers import PostCreateSerializer, PostSerializer, ScoreSerializer, ScoreCreateSerializer
from interview_task.settings import CACHE_MINUTE
from utils.metrics_common import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer

    def list(self, request, *args, **kwargs):
        Metrics.post_listed.inc()
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        Metrics.post_retrieved.inc()
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        Metrics.post_updated.inc()
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        Metrics.post_created.inc()
        return super().create(request, *args, **kwargs)


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ScoreCreateSerializer
        return ScoreSerializer

    @method_decorator(cache_page(CACHE_MINUTE))
    def retrieve(self, request, *args, **kwargs):
        Metrics.score_retrieved.inc()
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(cache_page(CACHE_MINUTE))
    def list(self, request, *args, **kwargs):
        Metrics.score_listed.inc()
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # serializer.save()
            value = request.data.get('value', 0)
            post_pk = request.data.get('post', 0)
            user_pk = request.data.get('user', 0)
            # post_obj = Post.objects.get(pk=post_pk)

            try:
                last_score = Score.objects.filter(
                    user__pk=user_pk, post__pk=post_pk).latest('scoredAt')
                last_score.value = value
                last_score.save()
                Metrics.score_created.inc()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Score.DoesNotExist:
                serializer.save()
                Metrics.score_updated.inc()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        Metrics.score_updated.inc()
        return super().update(request, *args, **kwargs)
