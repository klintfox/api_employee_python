from config import Config
from models import db
from controllers.employee_controller import employee_bp
from flask import Flask
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Crear las tablas al inicio
with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(employee_bp)

# Configuración de Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Ruta donde estará tu archivo swagger.json

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Employee API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
