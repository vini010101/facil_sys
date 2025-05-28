from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import ArtigoConhecimento, Treinamento


class ArtigoConhecimentoAdmin(ModelAdmin):
    model = ArtigoConhecimento
    menu_label = 'Artigos'
    menu_icon = 'doc-full'
    list_display = ('titulo', 'categoria', 'autor', 'data_criacao')
    search_fields = ('titulo', 'conteudo', 'categoria')
    ordering = ['-data_criacao']


class TreinamentoAdmin(ModelAdmin):
    model = Treinamento
    menu_label = 'Treinamentos'
    menu_icon = 'folder-open-inverse'
    list_display = ('modulo', 'titulo', 'criado_em')
    search_fields = ('modulo', 'titulo')
    ordering = ['-criado_em']


# Registrar os modelos no admin do Wagtail
modeladmin_register(ArtigoConhecimentoAdmin)
modeladmin_register(TreinamentoAdmin)
