from datetime import datetime

from flask_builder import db
from sqlalchemy_serializer import SerializerMixin


class {{cookiecutter.module_name|capitalize}}(db.Model, SerializerMixin):
    __tablename__ = '{{cookiecutter.module_name|lower}}s'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
