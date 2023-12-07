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

## Autenticación 🔐

El acceso a la API requiere autenticación básica. Las credenciales creadas son:

- username: admin - password: 1234

Es posible agregar nuevas credenciales en el archivo:

- `./src/app.py` en la variable `usuarios`

## API Reference 📖

### Productos

#### Lista todos los productos. 📋

```http
  GET /productos
```

#### Agrega un nuevo producto. 🆕

```http
  POST /api/items
```

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Required**. El nombre del producto         |
| `category`     | `string` | **Required**. La categoría del producto      |
| `stock`        | `integer` | **Required**. La cantidad de productos      |

#### Obtiene los detalles de un producto específico. 🔍

```http
  GET /productos/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del producto     |

#### Actualiza la información de un producto. 📝

```http
  PUT /productos/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del producto     |

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Optional**. El nombre del producto         |
| `category`     | `string` | **Optional**. La categoría del producto      |
| `stock`        | `integer` | **Optional**. La cantidad de productos      |

#### Elimina un producto del inventario. ❌

```http
  DELETE /productos/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del producto     |

### Categorías

#### Lista todas las categorías. 📋

```http
  GET /categorias
```

#### Crea una nueva categoría. 🆕

```http
  POST /categorias
```

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Required**. El nombre de la categoría      |

#### Muestra los productos en una categoría específica. 🔍

```http
  GET /categorias/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id de la categoría  |

#### Actualiza una categoría. 📝

```http
  PUT /categorias/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id de la categoría  |

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Required**. El nombre de la categoría      |

#### Elimina una categoría. ❌

```http
  DELETE /categorias/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id de la categoría  |
