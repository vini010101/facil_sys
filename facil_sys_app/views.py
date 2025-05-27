from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as auth_login
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import ArtigoConhecimento, ConteudoTreinamento, ModuloTreinamento
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser



#essa rota é responsavel por realizar o registro de um novo usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    #caso o usuario não forneça um usuario e senha ele recebe um erro informando a ausencia
    if not username or not password:
        return Response({'detail': 'Usuário e senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
    
    # faz uma consulta no banco e caso o usuario já estaja cadastrado ele recebe um erro
    if User.objects.filter(username=username).exists():
        return Response({'detail': 'Usuário já existe'}, status=status.HTTP_409_CONFLICT)
    
    #Cria um usuario no banco de dados
    user = User.objects.create_user(username=username, password=password)
    return Response({
        'detail': 'Usuário criado com sucesso',
        'user_id': user.id,
        'username': user.username
    }, status=status.HTTP_201_CREATED)

#essa rota é responsavel por realizar o login de um usuario
@api_view(['POST'])
@parser_classes([JSONParser])
@csrf_exempt
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Usei um If e else para valaidar os dados e fazer o login
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return Response({'detail': 'Login bem-sucedido'}, status=200)
    else:
        return Response({'detail': 'Credenciais inválidas'}, status=401)







@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
@csrf_exempt
def artigos_conhecimento_view(request):
    if request.method == 'GET':
        artigos = ArtigoConhecimento.objects.all().order_by('-data_criacao')
        data = []
        for artigo in artigos:
            data.append({
                'id': artigo.id,
                'titulo': artigo.titulo,
                'conteudo': artigo.conteudo,
                'categoria': artigo.categoria,
                'autor': artigo.autor.username if artigo.autor else None,
                'data_criacao': artigo.data_criacao,
                'data_atualizacao': artigo.data_atualizacao,
                'anexo': artigo.anexo.url if artigo.anexo else None,
            })
        return Response(data)

    elif request.method == 'POST':
        data = request.data

        # Validação manual dos campos obrigatórios
        titulo = data.get('titulo')
        conteudo = data.get('conteudo')
        categoria = data.get('categoria')

        if not titulo or not conteudo or not categoria:
            return Response({'error': 'Campos titulo, conteudo e categoria são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validar categoria entre as opções válidas
        categorias_validas = [c[0] for c in ArtigoConhecimento.CATEGORIAS]
        if categoria not in categorias_validas:
            return Response({'error': f'Categoria inválida. Opções válidas: {categorias_validas}'}, status=status.HTTP_400_BAD_REQUEST)

        autor = request.user if request.user.is_authenticated else None

        artigo = ArtigoConhecimento.objects.create(
            titulo=titulo,
            conteudo=conteudo,
            categoria=categoria,
            autor=autor,
        )

        # Não tratei arquivo (anexo) aqui, só JSON puro

        return Response({
            'id': artigo.id,
            'titulo': artigo.titulo,
            'conteudo': artigo.conteudo,
            'categoria': artigo.categoria,
            'autor': artigo.autor.username if artigo.autor else None,
            'data_criacao': artigo.data_criacao,
        }, status=status.HTTP_201_CREATED)
    








@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
@csrf_exempt
def conteudo_treinamento_view(request, modulo_id):
    try:
        modulo = ModuloTreinamento.objects.get(pk=modulo_id)
    except ModuloTreinamento.DoesNotExist:
        return Response({'error': 'Módulo não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        conteudos = modulo.conteudos.all().order_by('-data_criacao')
        data = []
        for c in conteudos:
            data.append({
                'id': c.id,
                'modulo_id': modulo.id,
                'tipo': c.tipo,
                'titulo': c.titulo,
                'texto': c.texto,
                'arquivo': c.arquivo.url if c.arquivo else None,
                'data_criacao': c.data_criacao,
            })
        return Response(data)

    elif request.method == 'POST':
        tipo = request.data.get('tipo')
        titulo = request.data.get('titulo')
        texto = request.data.get('texto')
        arquivo = request.FILES.get('arquivo')

        if not tipo or not titulo:
            return Response({'error': 'Campos tipo e titulo são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        tipos_validos = [t[0] for t in ConteudoTreinamento.TIPOS]
        if tipo not in tipos_validos:
            return Response({'error': f'Tipo inválido. Opções: {tipos_validos}'}, status=status.HTTP_400_BAD_REQUEST)

        if tipo in ['video', 'pdf'] and not arquivo:
            return Response({'error': 'Arquivo é obrigatório para tipo vídeo ou pdf.'}, status=status.HTTP_400_BAD_REQUEST)

        conteudo = ConteudoTreinamento.objects.create(
            modulo=modulo,
            tipo=tipo,
            titulo=titulo,
            texto=texto if tipo == 'texto' else None,
            arquivo=arquivo if tipo in ['video', 'pdf'] else None,
        )

        return Response({
            'id': conteudo.id,
            'tipo': conteudo.tipo,
            'titulo': conteudo.titulo,
            'texto': conteudo.texto,
            'arquivo': conteudo.arquivo.url if conteudo.arquivo else None,
            'data_criacao': conteudo.data_criacao,
        }, status=status.HTTP_201_CREATED)