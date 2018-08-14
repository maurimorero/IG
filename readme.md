### Dev instalation (Python 2.7)

* Install virtualenv (sudo apt-get install virtualenv)
* Create virtualenv (virtualenv yourvirtualenvname)
* Activate virtalenv (source ../yourvirtualenvname/bin/activate)
* In IG folder excecute `pip install -r requirements.txt`
* In IG folder excecute `python manage.py migrate`
* In IG folder excecute `python manage runserver`


### Request format
* Once loged in, en / page you have to specify the username to be consulted without @. There is no need to fill createdDate and status field (this will automatically completed by django)
