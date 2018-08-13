from django.conf.urls import url, include
from twitter.views import ProfileView


urlpatterns = [
    url('^(?P<id>.+)/$', ProfileView.as_view(), name='profile'),
]