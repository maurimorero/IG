# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from rest_framework import generics, viewsets
from twitter.serializers import TwitterProfileSerializer, RequestSerializer
from .models import TwitterProfile, Request
from django.http import Http404
from .tasks import GetTwitterProfile

class ProfileView(generics.ListAPIView):
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
        twitterProfile = TwitterProfile.objects.filter(username=request.username)
        if not twitterProfile:
            request.status = "Processing request"
            twitterProfile = GetTwitterProfile(request)
        else:
            twitterProfile = TwitterProfile.objects.filter(username=request.username)[0]
            request.status = "Completed"
        request.save()
        return redirect('twitter:profile',id=twitterProfile.id)







