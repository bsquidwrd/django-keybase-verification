from django.conf.urls import url
from keybase_verification.views import KeybaseVerificationView


urlpatterns = [
    url(r'^keybase.txt', KeybaseVerificationView.as_view()),
    url(r'^.well-known/keybase.txt', KeybaseVerificationView.as_view()),
]
