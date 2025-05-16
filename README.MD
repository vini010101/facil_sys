FacilSys
FacilSys é uma ferramenta interna desenvolvida para os colaboradores da Fácil Tecnologia. Seu principal objetivo é centralizar e organizar a consulta aos sistemas internos, promovendo uma navegação mais rápida, intuitiva e dinâmica.

Objetivo
Melhorar a eficiência do suporte técnico e das operações internas ao oferecer:

Acesso rápido e estruturado às funcionalidades dos sistemas da empresa;

Interface simples e responsiva para facilitar o uso no dia a dia;

Ponto central para visualização, autenticação e registro de informações operacionais.

Tecnologias Utilizadas
Backend: Django + Django REST Framework

Frontend: (A ser definido, ou deixar vazio se for só backend)

Banco de Dados: SQLite (para testes) / MySQL (em produção)

Autenticação: Sistema padrão do Django

Funcionalidades
Autenticação de usuários via API REST

Registro de novos colaboradores

Respostas padronizadas em JSON

Base inicial para integração com sistemas internos

Como rodar o projeto
Clone o repositório:

bash
Copiar
Editar
git clone <URL_DO_REPOSITORIO>
cd FacilSys
Crie um ambiente virtual e ative:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute as migrações:

bash
Copiar
Editar
python manage.py migrate
Inicie o servidor:

bash
Copiar
Editar
python manage.py runserver
Endpoints Principais
POST /api/login/ — Login do colaborador

POST /api/register/ — Registro de novo colaborador

Licença
Projeto interno de uso exclusivo da Fácil Tecnologia.

