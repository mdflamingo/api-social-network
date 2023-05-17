from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import include, path

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('v1/', include(router.urls)),


]
