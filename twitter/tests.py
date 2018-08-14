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
        request.username = "DiarioOle"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.name, "Diario Olé (@DiarioOle) | Twitter")

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


    def test_get_description(self):
        request = Request()
        request.username = "carlitostevez"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.description, "Jugador de Boca Juniors y Piola Vago frontman")

    def test_get_imageURI(self):
        request = Request()
        request.username = "carlitostevez"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        self.assertEqual(twitterProfile.imageURI, "https://pbs.twimg.com/profile_images/959194538182103041/q6heJEdD_400x400.jpg")


class RequestTests(TestCase):
    def test_request_pending(self):
        request = Request()
        request.username = "maurimorero"
        request.save()
        request = Request.objects.latest()
        self.assertEqual(request.status, "Pending")

    def test_request_completed(self):
        request = Request()
        request.username = "maurimorero"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        request = Request.objects.latest()
        self.assertEqual(request.status, "Completed")

    def test_request_account_suspended(self):
        request = Request()
        request.username = "pedronavajas"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        request = Request.objects.latest()
        self.assertEqual(request.status, "Account suspended")

    def test_request_account_not_found(self):
        request = Request()
        request.username = "pedronavajas1dwdaafdasdsafdsafasd"
        request.save()
        twitterProfile = GetTwitterProfile(request)
        request = Request.objects.latest()
        self.assertEqual(request.status, "User not found")