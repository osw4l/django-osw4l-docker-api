from django.db import models
from apps.utils.models import BaseModel
from django_lifecycle import AFTER_CREATE, hook, BEFORE_UPDATE


class Setup(BaseModel):
    allow_register = models.BooleanField(default=False)
    http_server_on = models.BooleanField(default=False)
    ws_server_on = models.BooleanField(default=False)
    twilio_key = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    twilio_account_sid = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    twilio_auth_token = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    from_email = models.EmailField(
        blank=True,
        null=True
    )
    payment_public_key = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    payment_private_key = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    payment_link_url = models.URLField(
        blank=True,
        null=True
    )
    frontend_url = models.URLField(
        blank=True,
        null=True
    )
    backend_url = models.URLField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    def __str__(self):
        return str(self.uuid)

