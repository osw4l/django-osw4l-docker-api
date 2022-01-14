from django.contrib import admin
from .models import Setup


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'updated_at',
        'http_server_on',
        'ws_server_on',
        'from_email',
        'frontend_url'
    ]

    def has_add_permission(self, request):
        return Setup.objects.count() == 0

    def has_delete_permission(self, request, obj=None):
        return False
