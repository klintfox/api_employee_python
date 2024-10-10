# Aqu� podr�as definir un esquema para validar y serializar datos
from marshmallow import Schema, fields, validate, ValidationError
import re

# Patrón para el campo email
email_pattern = r'^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\.cl$'
# Patrón para el campo password
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d.*\d).{8,}$'

class PhoneSchema(Schema):
    number = fields.String(
        required=True,
        validate=validate.Length(min=1, error="El número no puede estar vacío.")
    )
    citycode = fields.Integer(
        required=True,
        validate=validate.Range(min=0, error="El citycode no puede ser negativo.")
    )
    countrycode = fields.Integer(
        required=True,
        validate=validate.Range(min=0, error="El countrycode no puede ser negativo.")
    )

class EmployeeSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(
        required=True, 
        validate=validate.Regexp(
            email_pattern, 
            error='El correo electrónico debe seguir el formato: nombre@dominio.cl'
        )
    )
    password = fields.String(
        required=True, 
        validate=validate.Regexp(
            password_pattern, 
            error=(
                'La contraseña debe tener al menos 8 caracteres, '
                'contener al menos una letra mayúscula, '
                'una letra minúscula y al menos dos dígitos.'
            )
        )
    )
    phones = fields.List(fields.Nested(PhoneSchema), required=True)

try:
    employee = EmployeeSchema().load({
        'name': 'Juan Perez',
        'email': 'juan.perez@ejemplo.cl',
        'password': 'Contraseña123',
        'phones': [{'number': '123456789', 'citycode': 1, 'countrycode': 56}]
    })
    print(employee)
except ValidationError as err:
    print(err.messages)