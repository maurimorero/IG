# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from models import TwitterProfile, Request
from tasks import GetTwitterProfile

# Create your tests here.

class TwitterProfileTests(TestCase):

    def test_get_valid_profile1(self):
        request = Request()
        request.username = "maurimorero"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.name, "Mauricio Morero (@maurimorero) | Twitter")

    def test_get_valid_profile2(self):
        request = Request()
        request.username = "realDonaldTrump"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.name, "Donald J. Trump (@realDonaldTrump) | Twitter")

    def test_get_invalid_profile(self):
        request = Request()
        request.username = "gad78adsg8asdg98sd"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.id, -1)

    def test_get_suspended_profile(self):
        request = Request()
        request.username = "pedronavajas"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.id, -1)
