from dao.employee_dao import EmployeeDAO
from utils.messages import Messages

class EmployeeService:
    def __init__(self):
        self.dao = EmployeeDAO()
        
    def get_employee_by_email(self, email):
        return self.dao.get_employee_by_email(email)

    def create_employee(self, data):   
        return self.dao.add_employee(data)