from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de MySQL 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'productos_tecnologicos' 

# Inicializar MySQL
mysql = MySQL(app)

# Configuración de sesiones (para mensajes flash)
app.secret_key = 'mysecretkey'

# Ruta principal: Mostrar todos los productos
@app.route('/')
def index():
    cur = mysql.connection.cursor()  # Crear un cursor para interactuar con la base de datos
    cur.execute('SELECT * FROM productos')  # Consulta SQL para obtener todos los productos
    data = cur.fetchall()  # Obtener los resultados
    return render_template('index.html', productos=data)  # Renderizar la plantilla con los datos

# Ruta para mostrar el formulario de agregar producto
@app.route('/add')
def add():
    return render_template('add.html')

# Ruta para agregar un producto
@app.route('/add', methods=['POST'])
def add_product():
    if request.method == 'POST':  # Verificar si el método HTTP es POST
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']

        # Insertar los datos en la tabla `productos`
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)',
                    (nombre, descripcion, precio, stock))
        mysql.connection.commit()  # Guardar los cambios en la base de datos
        
        flash('Producto agregado exitosamente')  # Mostrar un mensaje de éxito
        return redirect(url_for('index'))  # Redirigir a la página principal

# Ruta para obtener un producto por ID (editar)
@app.route('/edit/<id>')
def get_product(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id,))  # Consulta SQL para obtener un producto específico
    data = cur.fetchone()  # Obtener el primer resultado
    return render_template('edit.html', producto=data)  # Renderizar la plantilla de edición con los datos

# Ruta para actualizar un producto
@app.route('/update/<id>', methods=['POST'])
def update_product(id):
    if request.method == 'POST':  # Verificar si el método HTTP es POST
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        cur = mysql.connection.cursor()
        # Actualizar los datos en la tabla `productos`
        cur.execute("""
            UPDATE productos
            SET nombre = %s, descripcion = %s, precio = %s, stock = %s
            WHERE id = %s
        """, (nombre, descripcion, precio, stock, id))
        mysql.connection.commit()  # Guardar los cambios en la base de datos
        flash('Producto actualizado exitosamente')  # Mostrar un mensaje de éxito
        return redirect(url_for('index'))  # Redirigir a la página principal

# Ruta para eliminar un producto
@app.route('/delete/<id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = %s', (id,))  # Consulta SQL para eliminar un producto
    mysql.connection.commit()  # Guardar los cambios en la base de datos
    flash('Producto eliminado exitosamente')  # Mostrar un mensaje de éxito
    return redirect(url_for('index'))  # Redirigir a la página principal

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)