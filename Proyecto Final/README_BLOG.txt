# Blog Django con Bootstrap

Este es un proyecto de blog desarrollado con Django, que incluye:

- Sistema de usuarios: Admin, Usuario Registrado, Usuario No Registrado.
- Registro e inicio de sesión.
- CRUD de publicaciones (crear, editar, eliminar).
- Filtros por autor, fecha de publicación y texto.
- Estilo visual con Bootstrap 5.

## 🚀 Requisitos

- Python 3.10+
- pip

## ⚙️ Instalación

1. Clonar o descomprimir el proyecto:

```
unzip blog_project.zip
cd blog_project
```

2. Crear un entorno virtual y activarlo:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar Django:

```bash
pip install django
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Crear un superusuario:

```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:

```bash
python manage.py runserver
```

## 🔐 Usuarios

- Usuarios no registrados: solo pueden ver publicaciones.
- Usuarios registrados: pueden crear, editar y borrar **sus propios** posts.
- Admins: tienen acceso completo desde el panel `/admin/`.

## 🌐 URLs importantes

- Página principal: http://127.0.0.1:8000/
- Registro: http://127.0.0.1:8000/register/
- Login: http://127.0.0.1:8000/accounts/login/
- Panel admin: http://127.0.0.1:8000/admin/

---

Este proyecto es una base para cualquier blog personal o sistema de publicación simple. ¡Podés seguir expandiéndolo con comentarios, imágenes, etiquetas y mucho más!
