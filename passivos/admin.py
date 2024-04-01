from django.contrib import admin

from passivos.models import Adiantamentos

@admin.register(Adiantamentos)
class AdiantamentoAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data', 'funcionario', 'descricao')
    list_filter = ('funcionario', 'data')
    search_fields = ('funcionario', 'data')
