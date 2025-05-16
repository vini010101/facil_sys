from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as auth_login
from rest_framework import status
from django.contrib.auth.models import User


#essa rota é responsavel por realizar o registro de um novo usuario
@api_view(['POST'])
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

