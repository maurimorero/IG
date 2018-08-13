from twitter.models import Request
from twitter.views import GetTwitterProfile


request= Request()
request.username='maurimorero'

GetTwitterProfile(request)

