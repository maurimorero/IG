# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from rest_framework import generics, viewsets
from twitter.serializers import TwitterProfileSerializer, RequestSerializer
from .models import TwitterProfile, Request
import urllib2
from bs4 import BeautifulSoup
from django.http import Http404
from .tasks import GetTwitterProfile

class ProfileView(generics.ListAPIView):
    #serializer_class = Serializer
    serializer_class = TwitterProfileSerializer
    def get_queryset(self):
        id = int(self.kwargs['id'])
        if id==-1:
            raise Http404
        return TwitterProfile.objects.filter(id=id)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    def create(self, request, *args, **kwargs):
        response = super(RequestViewSet, self).create(request, *args, **kwargs)
        request=Request.objects.latest()
        twitterProfile = GetTwitterProfile(request)
        return redirect('twitter:profile',id=twitterProfile.id)


def GetTwitterProfile1 (request):
    twitterProfile = TwitterProfile()
    url = "https://twitter.com/" + request.username
    try:
        page = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        twitterProfile.id =-1
        return twitterProfile
    soup = BeautifulSoup(page, "html.parser")
    endstring =soup.title.find('(')
    name= soup.title.text
    description = soup.findAll("p", {"class": "ProfileHeaderCard-bio"})[0].text
    imageURI = [x['src'] for x in soup.findAll('img', {'class': 'ProfileAvatar-image'})]
    followers = soup.findAll('span', {'class': 'ProfileNav-value'})[2]['data-count']
    twitterProfile.username = request.username
    twitterProfile.name = name
    twitterProfile.description = description
    twitterProfile.imageURI = imageURI
    twitterProfile.popularityIndex = followers
    twitterProfile.save()
    return twitterProfile






