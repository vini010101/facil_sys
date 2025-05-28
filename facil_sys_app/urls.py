from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.urls import path, include
from .views import login_user, register_user, artigos_conhecimento_view, treinamento_view
urlpatterns = [
    path('admin_site/', include(wagtailadmin_urls)),
    path('login/', login_user, name='login'),
    path('registro/', register_user, name='register'),
    path('novo_sys/', artigos_conhecimento_view, name='novo_sys'),
    path('treinamento/', treinamento_view, name='treimamento')
]
