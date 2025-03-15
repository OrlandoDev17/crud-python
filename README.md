# CRUD Productos Tecnológicos - Proyecto con Python y Flask

Este es un proyecto CRUD (Create, Read, Update, Delete) desarrollado para gestionar productos tecnológicos mediante una interfaz web construida con Python, Flask, MySQL (Configurado con XAMPP), HTML y CSS. El objetivo del proyecto es proporcionar una aplicación funcional y sencilla para administrar datos de productos

## Caracteristicas Principales

* **Interfaz CRUD completa:** Permite crear, leer, actualizar y eliminar registros de productos
* **Base de datos MySQL:** Utiliza MySQL como motor de base de datos, Configurado con XAMPP
* **Interfaz web simple:** Diseñada con HTML y CSS básico para un diseño limpio y responsivo
*  **Despliegue local rápido:** Configurado para ejecutarse fácilmente en un entorno de desarrollo local

## Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes herramientas:

* **[Python 3.x](https://www.python.org/downloads/)**
* **Pip (Administrador de Paquetes de Python)**
* **[XAMPP](https://www.apachefriends.org/es/download.html)**
*  **[Git](https://git-scm.com/downloads)**

## Dependencias del Proytecto

Las dependencias necesarias para este proyecto están listadas en el archivo requirements.txt. Puedes instalarlas ejecutando el siguiente comando

pip install -r requirements.txt

## Instalación y Configuración

**1- Clona el repositorio**

git clone https://github.com/OrlandoDev17/crud-python.git  
cd crud-productos-tecnologicos

**2- Configura la base de datos MySQL**

* Abre **XAMPP** y asegúrate de que los servicios **Apache** y **MySQL** estén activos
* Accede a **phpMyAdmin** en http://localhost/phpmyadmin .
* crea una nueva base de datos llamada **productos_tecnologicos**
* Importao crea manualmente la tabla **productos** con la siguiente estructura:

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

**3- Instala las dependencias** 

pip install -r requirements.txt

**4- Configura las credenciales de MySQL**
* Abre el archivo ***src/app.py*** y verifica que las credenciales de MySQL coincidan con tu configuración de XAMPP

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Por defecto, XAMPP no tiene contraseña para root
app.config['MYSQL_DB'] = 'productos_tecnologicos'

**5- Ejecuta la aplicación**

python src/app.py

**6- Accede a la aplicación**

Abre tu navegador y visita http://127.0.0.1:5000 para interactuar con el CRUD

## Estructura del Proyecto

El proyecto sigue una estructura organizada para facilitar su comprensión y mantenimiento.

crud-productos-tecnologicos/
│
├── src/                  # Carpeta principal del proyecto
│   ├── app.py            # Archivo principal de la aplicación Flask
│   ├── templates/        # Carpeta con plantillas HTML
│   │   ├── index.html    # Página principal (lista de productos)
│   │   ├── base.html     # Fragmentos de codigo reutilizables
│   │   ├── add.html     # Formulario para agregar un nuevo producto
|   |   ├── edit.html     # Formulario para editar un producto existente
│   │
│   ├── static/           # Archivos estáticos (CSS)
│   │   ├── styles.css    # Estilos personalizados
│
├── requirements.txt      # Lista de dependencias del proyecto
└── README.md             # Documentación del proyecto

## Uso del CRUD

**1- Crear un nuevo producto**

  * Haz click en el botón "Agregar Producto" en la pagina principal
  * Compelta el formulario y envíalo con el botón "Guardar"

**2- Ver todos los productos** 

  * En la página principal se pueden visualizar todos los productos con sus demas campos

**3- Actualizar un producto**

  * Haz clic en el botón "Editar" junto al producto que deseas modificar.
  * Actualiza los campos necesarios y guarda los cambios.

** 4- Eliminar un producto**

  * Haz clic en el botón "Eliminar" junto al producto que deseas borrar.

## Proyecto realizado por Orlando López
