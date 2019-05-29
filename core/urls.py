from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken

from core.views import SighupView, WordViewSet, VideoView

word_urls = [
    path("", WordViewSet.as_view({"get": "list", "post": "create"})),
    path("<pk>", WordViewSet.as_view({"put": "update", "delete": "destroy"})),
    path("<pk>/videos", VideoView.as_view())
]

urlpatterns = [
    path("login", ObtainAuthToken.as_view(), name="user_login"),
    path("sighup", SighupView.as_view(), name="user_sighup"),
    path("words/", include(word_urls)),
]
