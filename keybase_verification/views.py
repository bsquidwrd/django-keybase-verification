from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.sites.shortcuts import get_current_site

from keybase_verification.models import KeybaseVerification


class KeybaseVerificationView(View):
    def get(self, request):
        site = get_current_site(request)
        kbv = get_object_or_404(KeybaseVerification, site=site)
        return HttpResponse(kbv.data, content_type='text/plain')
