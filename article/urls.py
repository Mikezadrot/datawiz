from django.conf.urls import url
from django.urls import path
from .views import PostListView, PostDetailView

from rest_framework.routers import DefaultRouter
from account.viewsets import UserViewSet



urlpatterns = [

    path('', PostListView.as_view()),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]



# router = DefaultRouter()
# router.register(r"users", UserViewSet, basename="")
#
#
#
#
# # urlpatterns = router.urls
