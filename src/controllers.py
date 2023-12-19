import uuid
from flask import jsonify, request
from models import products, categories
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
        nuevo_producto["id"] = uuid.uuid4()
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
