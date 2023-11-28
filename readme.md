# API de Gestión de Inventario 📦

API de gestión de inventario desarrollada con Flask. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en productos y categorías, así como gestionar el inventario. El acceso a la API está protegido con autenticación básica.

## Comenzando 🚀

### Pre-requisitos 📋

- [Python 3.11](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)

### Instalación 🔧

2. Instalar las dependencias:
   ```
   pip install Flask Flask-HTTPAuth
   ```
2. Ejecutar la aplicación:
   ```
   python `./src/app.py`
   ```

## EndPoints 📖

Un endpoint es una URL específica donde la API REST puede ser accesible. Representa una función específica, se utiliza para realizar distintas operaciones en los recursos disponibles en el servicio web. Cada endpoint está asociado con una URL única y un método HTTP específico (GET, POST, PUT, DELETE, etc.).

### Productos

- **GET /productos**: Lista todos los productos. 📋
- **POST /productos**: Agrega un nuevo producto. 🆕

### Producto Específico

- **GET /productos/{id}**: Obtiene los detalles de un producto específico. 🔍
- **PUT /productos/{id}**: Actualiza la información de un producto. 📝
- **DELETE /productos/{id}**: Elimina un producto del inventario. ❌

### Categorías

- **GET /categorias**: Lista todas las categorías. 📋
- **POST /categorias**: Crea una nueva categoría. 🆕

### Categoría Específica

- **GET /categorias/{id}**: Muestra los productos en una categoría específica. 🔍
- **PUT /categorias/{id}**: Actualiza una categoría. 📝
- **DELETE /categorias/{id}**: Elimina una categoría. ❌

### Inventario

- **GET /inventario**: Muestra un resumen del inventario. 📊
- **POST /inventario**: Registra un cambio en el inventario (por ejemplo, un nuevo stock). 🔄

## Autenticación 🔐

El acceso a la API requiere autenticación básica. Las credenciales creadas son:

- username: admin - password: 1234

Es posible agregar nuevas credenciales en el archivo:

- `./src/app.py` en la variable `usuarios`
