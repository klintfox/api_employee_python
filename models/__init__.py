from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15), nullable=False)
    citycode = db.Column(db.Integer, nullable=False)
    countrycode = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phones = db.relationship('Phone', backref='employee', lazy=True)
