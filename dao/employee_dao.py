from models import db, Employee, Phone
from utils.messages import Messages

class EmployeeDAO:

    def get_employee_by_email(self, email):
       return Employee.query.filter_by(email=email).first()

    def add_employee(self, data):
        new_employee = Employee(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )

        db.session.add(new_employee)

        try:
            db.session.flush()  # Obtener el ID del empleado antes de agregar los teléfonos

            for phone_data in data.get('phones', []):
                new_phone = Phone(
                    number=phone_data['number'],
                    citycode=phone_data['citycode'],
                    countrycode=phone_data['countrycode'],
                    employee_id=new_employee.id
                )
                db.session.add(new_phone)

            db.session.commit()
            return {Messages.MESSAGE: Messages.EMPLOYEE_REGISTERED, Messages.STATUS: 201}  # Asegúrate de que esto sea un dict
            
        except Exception as e:
            db.session.rollback()
            print("Error al agregar el empleado:", str(e))
            return {Messages.MESSAGE: Messages.EMPLOYEE_REGISTER_ERROR.format(str(e))}, 500  # Este también debe ser un dict
