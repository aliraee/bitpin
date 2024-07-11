from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Post, Score
from .serializers import PostCreateSerializer, PostSerializer, ScoreSerializer, ScoreCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ScoreCreateSerializer
        return ScoreSerializer

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
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Score.DoesNotExist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
