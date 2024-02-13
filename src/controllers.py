import uuid
from flask import jsonify, request
from models import products, categories, users
from auth import auth

@auth.login_required
def handle_products():
    if request.method == 'GET':
        name = request.args.get('name')
        category = request.args.get('category')

        if name or category:
            filtered_products = [product for product in products if
                                (name is None or name.lower() in product['name'].lower()) and
                                (category is None or category.lower() in product['category'].lower())]
            return jsonify(filtered_products)
        else:
            return jsonify(products)
    elif request.method == 'POST':
        nuevo_producto = request.json
        nuevo_producto["id"] = str(uuid.uuid4())
        products.append(nuevo_producto)
        return jsonify(nuevo_producto), 201

@auth.login_required
def handle_product(id):
    producto = next((p for p in products if p['id'] == id), None)
    if not producto:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

    if request.method == 'GET':
        return jsonify(producto)
    elif request.method == 'PUT':
        datos = request.json
        producto.update(datos)
        return jsonify(producto)
    elif request.method == 'DELETE':
        products.remove(producto)
        return jsonify({'mensaje': 'Producto eliminado'}), 200

@auth.login_required
def handle_categories():
    if request.method == 'GET':
        return jsonify(categories)
    elif request.method == 'POST':
        nueva_categoria = request.json
        nueva_categoria["id"] = uuid.uuid4()
        categories.append(nueva_categoria)
        return jsonify(nueva_categoria), 201

@auth.login_required
def handle_category(id):
    categoria = next((c for c in categories if c['id'] == id), None)
    if not categoria:
        return jsonify({'mensaje': 'Categoría no encontrada'}), 404

    if request.method == 'GET':
        products_en_categoria = [p for p in products if p['categoria'] == categoria['nombre']]
        return jsonify(products_en_categoria)
    elif request.method == 'PUT':
        datos = request.json
        categoria.update(datos)
        return jsonify(categoria)
    elif request.method == 'DELETE':
        categories.remove(categoria)
        return jsonify({'mensaje': 'Categoría eliminada'}), 200

@auth.login_required
def handle_users():
    if request.method == 'GET':
        return jsonify(users)
    elif request.method == 'POST':
        new_user = request.json
        new_user["id"] = uuid.uuid4()
        categories.append(new_user)
        users.append(new_user)
        return jsonify(new_user), 201

@auth.login_required
def handle_user(id: str):
    user_data = next((u for u in users if u['id'] == id), None)
    if not user_data:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    if request.method == 'GET':
        name = request.args.get('role')

        if name:
            users = [
                user for user in users if
                (name is None or name.lower() in users['role'].lower())
            ]
            return jsonify(users)
        else:
            return jsonify(users)
    elif request.method == 'PUT':
        user_data = request.json
        users.update(user_data)
        return jsonify(user_data), 201
    elif request.method == 'DELETE':
        categories.remove(user_data)
        return jsonify({'mensaje': 'Usuario eliminada'}), 200