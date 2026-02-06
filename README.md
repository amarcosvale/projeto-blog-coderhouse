# Antonio Vale - PF - Blog

## Sobre o projeto
Este é um projeto de blog desenvolvido em Django, com funcionalidades de páginas estáticas, autenticação de usuários e administração via painel do Django.

## Funcionalidades
- Home
- About (Sobre)
- Lista de páginas
- Criar página
- Editar página
- Excluir página
- Login / Logout
- Registro de usuários
- Admin (painel administrativo do Django)

## Estrutura de diretórios principais
- `pages/` - App de páginas do blog
- `accounts/` - App de autenticação e gerenciamento de usuários
- `templates/` - Templates HTML do projeto
- `media/` - Arquivos de mídia (imagens)
- `static/` - Arquivos estáticos (CSS, JS)
- `db.sqlite3` - Banco de dados SQLite
- `manage.py` - Script de gerenciamento do Django

## URLs importantes
- Home: `/`
- About: `/about/`
- Lista de páginas: `/pages/`
- Criar página: `/pages/create/`
- Editar página: `/pages/<id>/update/`
- Excluir página: `/pages/<id>/delete/`
- Login: `/accounts/login/`
- Logout: `/accounts/logout/`
- Registrar usuário: `/accounts/signup/`
- Admin: `/admin/`

## Observações
- Para criar páginas, é necessário estar logado.
- O campo de imagem é opcional.
- As páginas criadas são associadas ao usuário que as criou.

## Como rodar o projeto
1. Clonar o repositório:  
   ```bash
   git clone <https://github.com/amarcosvale/projeto-blog-coderhouse.git>
2. Entrar no diretório do projeto: cd projeto_blog_coderhouse
3. Ativar o ambiente virtual: venv\Scripts\activate
4. Instalar dependências: pip install -r requirements.txt
5. Aplicar migrações: python manage.py migrate
6. Criar superusuário: python manage.py createsuperuser
7. Rodar o servidor: python manage.py runserver
8. Acessar o projeto pelo navegador: http://127.0.0.1:8000/
