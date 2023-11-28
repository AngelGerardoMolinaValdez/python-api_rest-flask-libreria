from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

usuarios = {
    "admin": "1234"
}

productos = [
    {"id": 1, "nombre": "Producto 1", "categoria": "Electrónica", "stock": 10},
    {"id": 2, "nombre": "Producto 2", "categoria": "Ropa", "stock": 20},
]

categorias = [
    {"id": 1, "nombre": "Electrónica"},
    {"id": 2, "nombre": "Ropa"},
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
        productos.append(nuevo_producto)
        return jsonify(nuevo_producto), 201

@app.route('/productos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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
        categorias.append(nueva_categoria)
        return jsonify(nueva_categoria), 201

@app.route('/categorias/<int:id>', methods=['GET', 'PUT', 'DELETE'])
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

@app.route('/inventario', methods=['GET', 'POST'])
@auth.login_required
def manejar_inventario():
    if request.method == 'GET':
        resumen = {
            'total_productos': len(productos),
            'categorias': [c['nombre'] for c in categorias]
        }
        return jsonify(resumen)
    elif request.method == 'POST':
        nuevo_id = len(categorias) + 1
        cambio_inventario = request.json
        nueva_categoria = {"id": nuevo_id, "nombre": cambio_inventario["nombre"]}
        return jsonify({'mensaje': 'Inventario actualizado'}), 201

# Para ejecutar la app
app.run(debug=True)
