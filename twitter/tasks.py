from celery import shared_task
from .models import TwitterProfile
import urllib2
from bs4 import BeautifulSoup

@shared_task
def GetTwitterProfile (request):
    request.status="Procesing"
    request.save()
    twitterProfile = TwitterProfile()
    url = "https://twitter.com/" + request.username
    try:
        page = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        twitterProfile.id =-1
        request.status = "User not found"
        request.save()
        return twitterProfile
    soup = BeautifulSoup(page, "html.parser")
    checkAccountSuspended = soup.h1.text
    if (checkAccountSuspended=="Cuenta suspendida") or (checkAccountSuspended=="Account suspended"):
        twitterProfile.id = -1
        request.status = "Account suspended"
        request.save()
        return twitterProfile
    name= soup.title.text
    description = soup.findAll("p", {"class": "ProfileHeaderCard-bio"})[0].text
    imageURI = [x['src'] for x in soup.findAll('img', {'class': 'ProfileAvatar-image'})][0]
    followers = soup.findAll('span', {'class': 'ProfileNav-value'})[2]['data-count']
    twitterProfile.username = request.username
    twitterProfile.name = name
    twitterProfile.description = description
    twitterProfile.imageURI = imageURI
    twitterProfile.popularityIndex = followers
    twitterProfile.save()
    request.status = "Completed"
    request.save()
    return twitterProfile