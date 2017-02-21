=====
Keybase Verification
=====

Keybase Verification is a simple Django app to allow easy verification of your domain for [keybase.io](http://keybase.io).
For each site, you will be able to create an record containing the verification information required by Keybase

Quick start
-----------

* Add "keybase_verification" and "django.contrib.sites" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'keybase_verification',
]
```

* Include the polls URLs in your project urls.py like this::

```python
from keybase_verification.views import KeybaseVerificationView

urlpatterns = [
    ...
    url(r'^keybase.txt', KeybaseVerificationView.as_view()),
    url(r'^.well-known/keybase.txt', KeybaseVerificationView.as_view()),
]
```

* Run `python manage.py migrate` to create the polls models.

* Start the development server and visit http://127.0.0.1:8000/admin/ to create a site with the URL you are wanting to verify (in this case 127.0.0.1), then create a Keybase Verification for a particular site (you'll need the Admin app enabled).

* Visit http://127.0.0.1:8000/keybase.txt or http://127.0.0.1:8000/.well-known/keybase.txt to view your proof.
