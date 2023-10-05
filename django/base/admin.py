from django.contrib import admin, messages
from base.models import Contato

@admin.action(description="marcar como lido")
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.messege_user(request, "marcado com lido!", messages.SUCCESS)

@admin.register(Contato )
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome','email', 'data']
    list_filter = ['data']
    search_fields = ['nome', 'email']
    actions = [marcar_como_lido]