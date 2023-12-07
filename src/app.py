from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import uuid

def create_app(test_config=None):
    app = Flask(__name__)
    auth = HTTPBasicAuth()

    if test_config:
        app.config.update(test_config)

    usuarios = {
        "admin": "1234"
    }

    productos = [
        {
            "id": "c1e4db67-f958-4779-9fd1-1e7680a6d3dd",
            "name": "Producto 1",
            "category": "Electrónica",
            "stock": 10
        },
        {
            "id": "c7a04c63-eac7-4d07-87b7-4985b61cc443",
            "name": "Producto 2",
            "category": "Ropa", 
            "stock": 20
        },
    ]

    categorias = [
        {
            "id": 1,
            "name": "Electrónica"},
        {
            "id": 2,
            "name": "Ropa"
        }
    ]

    @auth.verify_password
    def verificar_credenciales(username, password):
        if username in usuarios and usuarios[username] == password:
            return username

    # Endpoints
    @app.route('/productos', methods=['GET', 'POST'])
    @auth.login_required
    def manejar_productos():
        if request.method == 'GET':
            return jsonify(productos)
        elif request.method == 'POST':
            nuevo_producto = request.json
            nuevo_producto["id"] = uuid.uuid4()
            productos.append(nuevo_producto)
            return jsonify(nuevo_producto), 201

    @app.route('/productos/<string:id>', methods=['GET', 'PUT', 'DELETE'])
    @auth.login_required
    def manejar_producto(id):
        producto = next((p for p in productos if p['id'] == id), None)
        if not producto:
            return jsonify({'mensaje': 'Producto no encontrado'}), 404

        if request.method == 'GET':
            return jsonify(producto)
        elif request.method == 'PUT':
            datos = request.json
            producto.update(datos)
            return jsonify(producto)
        elif request.method == 'DELETE':
            productos.remove(producto)
            return jsonify({'mensaje': 'Producto eliminado'}), 200

    @app.route('/categorias', methods=['GET', 'POST'])
    @auth.login_required
    def manejar_categorias():
        if request.method == 'GET':
            return jsonify(categorias)
        elif request.method == 'POST':
            nueva_categoria = request.json
            nueva_categoria["id"] = uuid.uuid4()
            categorias.append(nueva_categoria)
            return jsonify(nueva_categoria), 201

    @app.route('/categorias/<string:id>', methods=['GET', 'PUT', 'DELETE'])
    @auth.login_required
    def manejar_categoria(id):
        categoria = next((c for c in categorias if c['id'] == id), None)
        if not categoria:
            return jsonify({'mensaje': 'Categoría no encontrada'}), 404

        if request.method == 'GET':
            productos_en_categoria = [p for p in productos if p['categoria'] == categoria['nombre']]
            return jsonify(productos_en_categoria)
        elif request.method == 'PUT':
            datos = request.json
            categoria.update(datos)
            return jsonify(categoria)
        elif request.method == 'DELETE':
            categorias.remove(categoria)
            return jsonify({'mensaje': 'Categoría eliminada'}), 200
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
