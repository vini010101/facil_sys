
from django.urls import path
from .views import login_user, register_user, artigos_conhecimento_view, treinamento_view
urlpatterns = [
    path('login/', login_user, name='login'),
    path('registro/', register_user, name='register'),
    path('novo_sys/', artigos_conhecimento_view, name='novo_sys'),
    path('treinamento/', treinamento_view, name='treimamento')
]
