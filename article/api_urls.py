from rest_framework_extensions.routers import ExtendedDefaultRouter

from .viewsets import PostViewSet, CommentViewSet
router = ExtendedDefaultRouter()


post_router = router.register(r'posts', PostViewSet, 'posts')

post_router.register("comments", CommentViewSet, basename='comments', parents_query_lookups=['post_id'])
# router.register(r"posts")

comments_router = post_router.register(r'comments', CommentViewSet, basename='comments', parents_query_lookups=['post_id'])

urlpatterns = router.urls
