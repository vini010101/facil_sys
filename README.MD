# 🛠️ FacilSys – Plataforma Interna para Suporte Técnico

**FacilSys** é um sistema interno desenvolvido para **centralizar o conhecimento técnico**, melhorar a **autonomia dos técnicos de suporte** e **padronizar procedimentos operacionais** dentro da empresa **Fácil Tecnologia**.

---

## 📌 Sobre o Projeto

Durante minha atuação como Técnico de Suporte N1, observei problemas recorrentes na rotina de atendimento:

- Repetição constante de dúvidas operacionais
- Falta de uma central de consulta rápida e confiável
- Documentação dispersa ou inexistente
- Perda de tempo e produtividade por falta de padronização

O **FacilSys** foi criado para resolver esses problemas, permitindo que os técnicos consultem **tutoriais, normas e sistemas internos** de forma rápida e intuitiva.

---

## 🎯 Funcionalidades

- ✅ Cadastro e exibição de artigos técnicos
- ✅ Filtro por categoria, data, autor e palavras-chave
- ✅ Área de sistemas internos com links e descrições
- ✅ Busca dinâmica por título ou conteúdo
- ✅ Painel administrativo com autenticação
- ✅ Interface leve e responsiva
  ✅ envio automatico de E-mail com atulização sobre Normal e Treinametos para os colaboradores ( Em Desenvolvimento )

---

## ⚙️ Tecnologias Utilizadas

| Camada         | Tecnologia               |
|----------------|--------------------------|
| Backend        | Python + Django          |
| Banco de Dados | SQLite (versão inicial)  |
| Frontend       | HTML + BootStrap CSS + JS |
| Deploy         | Docker (em planejamento) |
| Ambiente       | Projeto local ou VPS     |

---

## 🧪 Status do Projeto

✅ Projeto funcional  
🚧 Implantação na empresa em avaliação  
🔄 Em constante manutenção e evolução pessoal

---

## 📂 Instalação (modo local)

1. Clone o repositório:
```bash
git clone https://github.com/viniciuscalebe/facil_sys.git
cd facilsys

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
Acesse em http://127.0.0.1:8000/


👨‍💻 Autor
Vinicius Calebe Barbosa de Moura
Desenvolvedor Backend Python

🧠 Lições Aprendidas
Transformar problemas reais em soluções técnicas práticas

Uso avançado do Django com ORM, views, templates e admin

Organização de código para manutenção e escalabilidade

Comunicação técnica com gestão e apresentação de projetos
