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
   pip install Flask Flask-HTTPAuth assertpy
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
  GET /products
```

##### Path Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Optional**. El nombre del producto         |
| `category`     | `string` | **Optional**. La categoría del producto      |

#### Agrega un nuevo producto. 🆕

```http
  POST /products
```

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Required**. El nombre del producto         |
| `category`     | `string` | **Required**. La categoría del producto      |
| `stock`        | `integer` | **Required**. La cantidad de productos      |

#### Obtiene los detalles de un producto específico. 🔍

```http
  GET /products/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del producto     |

#### Actualiza la información de un producto. 📝

```http
  PUT /products/{id}
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
  DELETE /products/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del producto     |

### Categorías

#### Lista todas las categorías. 📋

```http
  GET /categories
```

#### Crea una nueva categoría. 🆕

```http
  POST /categories
```

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `name`         | `string` | **Required**. El nombre de la categoría      |

#### Muestra los productos en una categoría específica. 🔍

```http
  GET /categories/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id de la categoría  |

#### Actualiza una categoría. 📝

```http
  PUT /categories/{id}
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
  DELETE /categories/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id de la categoría  |

### Usuarios

#### Lista todos los usuarios. 📋

```http
  GET /users
```

##### Path Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `role`         | `string` | **Optional**. El rol del usuario             |

#### Crear un nuevo usuario. 🆕

```http
  POST /users
```

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `username`         | `string` | **Required**. El nombre de usuario        |
| `password`     | `string` | **Required**. La contraseña      |
| `role`        | `integer` | **Required**. El rol del usuario      |
| `name`        | `integer` | **Required**. El nombre del usuario      |
| `address`        | `integer` | **Required**. La dirección del usuario      |
| `email`        | `integer` | **Required**. El correo del usuario      |

#### Obtiene los detalles de un producto específico. 🔍

```http
  GET /users/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del usuario     |

#### Actualiza la información de un usuario. 📝

```http
  PUT /users/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del usuario     |

##### Query Parameters

| Parameter      | Type     | Description                                  |
| :------------- | :------- | :------------------------------------------- |
| `username`         | `string` | **Required**. El nombre de usuario        |
| `password`     | `string` | **Required**. La contraseña      |
| `role`        | `integer` | **Required**. El rol del usuario      |
| `name`        | `integer` | **Required**. El nombre del usuario      |
| `address`        | `integer` | **Required**. La dirección del usuario      |
| `email`        | `integer` | **Required**. El correo del usuario      |

#### Eliminar un usuario. ❌

```http
  DELETE /usuario/{id}
```

##### Path Parameters

| Parameter    | Type      | Description                          |
| :----------- | :-------  | :----------------------------------- |
| `id`         | `string`  | **Required**. el id del usuario     |