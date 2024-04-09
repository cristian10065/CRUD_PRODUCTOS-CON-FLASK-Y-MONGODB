
from flask import Flask, render_template, request, redirect, url_for
import database as dbase  
from producto import Producto

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    productos = db['productos']
    productoReceived = productos.find()
    return render_template('index.html', productos = productoReceived)

#Method Post
@app.route('/productos', methods=['POST'])
def addProducto():
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        producto = Producto(nombre, precio, cantidad)
        productos.insert_one(producto.toDBCollection())
        return redirect(url_for('home'))
    else:
        return "Algo estas haciando mal"

#Method delete
@app.route('/eliminar/<string:producto_nombre>')
def eliminar(producto_nombre):
    productos= db['productos']
    productos.delete_one({'nombre' : producto_nombre})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:producto_nombre>', methods=['POST'])
def edit(producto_nombre):
    productos = db['productos']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    if nombre and precio and cantidad:
        productos.update_one({'nombre' : producto_nombre}, {'$set' : {'nombre' : nombre, 'precio' : precio, 'cantidad' : cantidad}})
        return redirect(url_for('home'))
    else:
        return "Hay algo mal"

if __name__ == '__main__':
    app.run(debug=True, port=4000)
