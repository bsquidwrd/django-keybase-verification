from django.test import TestCase, RequestFactory
from django.contrib.sites.models import Site

from .models import KeybaseVerification
from .views import KeybaseVerificationView

class KeybaseVerificationTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        # Create Site and KeybaseVerification model to test with
        self.site = Site.objects.create(domain='testserver')
        self.kbv = KeybaseVerification.objects.create(site=self.site, data='Test client Keybase Verification')

    def test_base_text_file(self):
        # Request and Response for the Keybase Verification url
        request = self.factory.get('/keybase.txt')
        response = KeybaseVerificationView.as_view()(request)

        # Assert the status code is 200 and the content is the same as created
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Test client Keybase Verification')

    def test_well_known_text_file(self):
        # Request and Response for the Keybase Verification url
        request = self.factory.get('/.well-known/keybase.txt')
        response = KeybaseVerificationView.as_view()(request)

        # Assert the status code is 200 and the content is the same as created
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Test client Keybase Verification')
