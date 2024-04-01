from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'nome', 'sobrenome', 'is_staff', 'ativo']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'sobrenome')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'nome', 'sobrenome']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
