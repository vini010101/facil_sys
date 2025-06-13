from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import ArtigoConhecimento, Treinamento, Convenios


class ArtigoConhecimentoAdmin(ModelAdmin):
    model = ArtigoConhecimento
    menu_label = 'Editar SYS'
    menu_icon = 'doc-full'
    list_display = ('titulo', 'categoria', 'autor', 'data_criacao')
    search_fields = ('titulo', 'conteudo', 'categoria')
    ordering = ['-data_criacao']


class TreinamentoAdmin(ModelAdmin):
    model = Treinamento
    menu_label = 'Editar Treinamentos'
    menu_icon = 'folder-open-inverse'
    list_display = ('modulo', 'titulo', 'criado_em')
    search_fields = ('modulo', 'titulo')
    ordering = ['-criado_em']


class Convenios(ModelAdmin):
   model = Convenios
   menu_label = 'Editar Convenios'
   menu_icon = 'folder-open-inverse'
   list_display = ('nome', 'conteudo', 'criado_em')
   search_fields = ('nome', 'conteudo')
   ordering = ['-criado_em']  

# Registrar os modelos no admin do Wagtail
modeladmin_register(ArtigoConhecimentoAdmin)
modeladmin_register(TreinamentoAdmin)
modeladmin_register(Convenios)
