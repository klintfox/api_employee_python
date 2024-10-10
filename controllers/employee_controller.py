from flask import Blueprint, request, jsonify
from flasgger import swag_from
from pydantic import BaseModel, EmailStr, constr
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from schemas.employee_schema import EmployeeSchema
from services.employee_service import EmployeeService
from utils.messages import Messages


employee_bp = Blueprint('employee', __name__)
service = EmployeeService()

@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    schema = EmployeeSchema()
    data = request.get_json()
    print("Datos recibidos:", data)

    try:
        # Validar los datos usando el esquema
        validated_data = schema.load(data)
        
        # Verificar si el correo ya existe antes de llamar al servicio
        existing_user = service.get_employee_by_email(validated_data['email'])
        if existing_user:
            return jsonify({Messages.MESSAGE: Messages.EMPLOYEE_ALREADY_REGISTERED}), 409
        
        # Si el correo no existe, proceder a crear el empleado
        result = service.create_employee(validated_data)
        return jsonify(result), 201  # Retorna 201 si se crea correctamente
        
    except ValidationError as err:
        return jsonify({Messages.MESSAGE: err.messages}), 400
    except Exception as e:
        print("Error interno:", str(e))
        return jsonify({Messages.MESSAGE: Messages.INTERNAL_SERVER_ERROR}), 500