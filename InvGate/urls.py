
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from twitter.views import RequestViewSet

router = routers.DefaultRouter()
router.register(r'', RequestViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^twitter/', include('twitter.urls',namespace= "twitter")),
]
