# API_Employee_Python
API en python para gestionar el registro de un empleado en una base de datos SQLAlchemy.


## Clonar y configurar proyecto
1. Clonar proyecto git y posicionarse sobre la carpeta del proyecto.
```sh
git clone https://github.com/klintfox/api_employee_python
```
2. Crea un entorno virtual
Esto es opcional, pero se recomienda para manejar las dependencias.
```sh 
python -m venv venv 
```
3. Activa el entorno virtual
En Windows:
```sh
venv\Scripts\activate
```
4. Instala las dependencias
Asegúrate de que tengas un archivo requirements.txt. Si lo tienes, ejecuta:
```sh
pip install -r requirements.txt
```
##
ejecutar proyecto 
```sh
python app.py
```
## Pruebas
- Ingresar en el navegador e ir a http://localhost:5000/swagger/#/default/post_employees
Esquema
```sh
{
  "name": "Peter",
  "email": "Peter@example.cl",
  "password": "Peter123",
  "phones": [
    {
      "number": "12345678",
      "citycode": 1,
      "countrycode": 57
    }
  ]
}
```

### Documentación de la API con Flasgger
Para documentar nuestra API, utilizamos Flasgger, una extensión de Flask que facilita la creación de documentación Swagger para APIs RESTful.

### ¿Qué es Flasgger?
Flasgger permite integrar Swagger UI en aplicaciones Flask, proporcionando una interfaz interactiva donde los desarrolladores pueden explorar y probar la API de manera sencilla. Swagger es un marco de trabajo popular para documentar APIs, permitiendo que los consumidores de la API entiendan rápidamente cómo interactuar con ella.
Para instalar Flasgger, puedes utilizar pip:
```sh
pip install flasgger
```
### Schema

**Validación de datos:** Se crea el archivo employee_schema.py el cual define un esquema de validación para los datos que se envían al API, usando herramientas como Marshmallow o Pydantic. Es responsable de verificar que los datos que recibe el API cumplan con las expectativas antes de procesarlos.

**Lógica de Negocio:** Ayuda a asegurar que los datos son correctos y en el formato adecuado, facilitando el manejo de errores antes de que lleguen a la lógica de negocio.

### Documentación de API

El archivo swagger.json creado es una forma de definir la documentación del API en un formato estructurado que puede ser interpretado por herramientas de Swagger. Algunas razones por las cuales podrías querer tener este archivo:

1. <span style="color: green;">**Especificación Estándar**</span>
Formato Swagger: Utilizar el formato Swagger (OpenAPI Specification) permite describir tu API de manera estándar, lo que facilita la comprensión para otros desarrolladores y herramientas que pueden interactuar con tu API.
2. <span style="color: green;">**Interoperabilidad**</span>
Compatibilidad: Muchos clientes y herramientas de API (como Postman, Swagger UI, y otros) pueden leer y generar documentación y código cliente a partir de este archivo, lo que aumenta la interoperabilidad.
3. <span style="color: green;">**Desarrollo de la API**</span>
Referencia Rápida: El archivo actúa como una referencia rápida para el desarrollo, ya que todos los endpoints, parámetros y respuestas están documentados en un solo lugar.
4. <span style="color: green;">**Facilidad de Pruebas**</span>
Testing: Puedes utilizar herramientas que leen esta especificación para probar automáticamente tu API, asegurando que se comporta de acuerdo con la documentación.
5. <span style="color: green;">**Actualizaciones Simples**</span>
Mantenimiento: Si realizas cambios en tu API, puedes actualizar el archivo swagger.json en lugar de tener que modificar múltiples documentos o secciones.


### Libreria Utilizadas
1. <span style="color: green;">**Flask**</span>
Es un microframework para Python que permite crear aplicaciones web. Proporciona las herramientas y bibliotecas necesarias para manejar solicitudes HTTP, enrutamiento, plantillas, y más.
Uso en tu código: Se usa para definir la aplicación principal y manejar las rutas y solicitudes.
2. <span style="color: green;">**Flasgger**</span>
Es una extensión de Flask que simplifica la integración de Swagger para documentar APIs. Permite generar documentación interactiva para tus endpoints.
Uso en tu código: Se usa para definir y servir la documentación de la API, y para configurar Swagger en tu aplicación.
3. <span style="color: green;">**Flask-Swagger-UI**</span>
Es una extensión que proporciona una interfaz de usuario para la documentación Swagger de tu API. Permite visualizar y probar los endpoints de la API directamente desde un navegador.
Uso en tu código: Se utiliza para servir la interfaz de Swagger UI, que permite a los usuarios interactuar con la API de manera visual.
4. <span style="color: green;">**Pydantic**</span>
Es una biblioteca de validación de datos y configuración basada en tipos de Python. Proporciona un modelo de datos que se puede utilizar para validar y serializar datos fácilmente.
Uso en tu código: Se utiliza para definir esquemas de validación de datos para las solicitudes a la API, como el modelo de empleado.
5. <span style="color: green;">**Marshmallow**</span>
Es una biblioteca de serialización/deserialización de objetos complejos a formatos simples como JSON. También permite la validación de datos.
Uso en tu código: Se utiliza para validar y transformar los datos de entrada de las solicitudes en esquemas definidos.
6. <span style="color: green;">**QLAlchemy** (implícito en db)</span>
Es un ORM (Object Relational Mapper) para Python que permite interactuar con bases de datos de manera más intuitiva mediante el uso de objetos.
Uso en tu código: Proporciona las herramientas para definir modelos de base de datos y realizar consultas.
7. <span style="color: green;">**Blueprint** (de Flask)</span>
Es una forma de organizar tu aplicación Flask en módulos. Permite definir rutas y manejadores de manera modular, facilitando la escalabilidad.
Uso en tu código: Se utiliza para crear el blueprint del controlador de empleados, permitiendo registrar rutas relacionadas.
8. <span style="color: green;">**Config** (implícito en config)</span>
Normalmente, es una clase o archivo que contiene la configuración de la aplicación, como variables de entorno, configuraciones de base de datos, etc.
Uso en tu código: Se utiliza para cargar la configuración de la aplicación Flask.