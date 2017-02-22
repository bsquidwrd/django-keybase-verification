from django.db import models
from django.contrib.sites.models import Site


class KeybaseVerification(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    data = models.TextField(blank=True, null=True, help_text="Get this by visiting http://keybase.io")

    def __str__(self):
        return 'Keybase Verification for {}'.format(self.site.domain)

    class Meta:
        verbose_name = 'Keybase Verification'
        verbose_name_plural = 'Keybase Verification'
