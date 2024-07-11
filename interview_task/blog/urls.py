from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ScoreViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]