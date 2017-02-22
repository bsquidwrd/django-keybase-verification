=====
Keybase Verification [![Build Status](https://travis-ci.org/bsquidwrd/django-keybase-verification.svg?branch=master)](https://travis-ci.org/bsquidwrd/django-keybase-verification)
=====

Keybase Verification is a simple Django app to allow easy verification of your domain for [keybase.io](http://keybase.io).
For each site, you will be able to create a record containing the verification information required by Keybase.

Quick start
-----------

* Install the package with `pip install django-keybase-verification`

* Add "keybase_verification" and "django.contrib.sites" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'keybase_verification',
]
```

* Include the Keybase URLs in your project urls.py and make sure to import the `django.conf.urls.include` method like this:

```python
from django.conf.urls import url, include

urlpatterns = [
    ...
    url(r'^', include('keybase_verification.urls')),
]
```

* Run `python manage.py migrate` to create the keybase_verification models.

* Start the development server and visit http://127.0.0.1:8000/admin/ to create a site with the URL you are wanting to verify (in this case 127.0.0.1), then create a Keybase Verification for a particular site (you'll need the Admin app enabled).

* Visit http://127.0.0.1:8000/keybase.txt or http://127.0.0.1:8000/.well-known/keybase.txt to view your proof.
