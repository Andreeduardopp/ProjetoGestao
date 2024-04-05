from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = (
        'email',
        'username',
    )
    filter_horizontal = ('user_permissions', 'groups')
