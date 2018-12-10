from datetime import datetime
from flask import Blueprint
from lib.utils import setattrs, success
from webargs.flaskparser import use_kwargs
from flask_builder import db
from flasgger import swag_from

from .spec import {{cookiecutter.module_name|upper}}S_LIST, {{cookiecutter.module_name|upper}}_BY_ID, {{cookiecutter.module_name|upper}}_CREATE, {{cookiecutter.module_name|upper}}_UPDATE, {{cookiecutter.module_name|upper}}_DELETE
from .models import {{cookiecutter.module_name|capitalize}}
from .schemas import FILTER_{{cookiecutter.module_name|upper}}S_SCHEMA, ADD_{{cookiecutter.module_name|upper}}_SCHEMA, UPDATE_{{cookiecutter.module_name|upper}}_SCHEMA

mod = Blueprint('{{cookiecutter.module_name|lower}}s', __name__, url_prefix='/{{cookiecutter.module_name|lower}}s')


@mod.route('/')
@swag_from({{cookiecutter.module_name|upper}}S_LIST)
@use_kwargs(FILTER_{{cookiecutter.module_name|upper}}S_SCHEMA)
def list_view(page, limit, sort_by):
    q = {{cookiecutter.module_name|capitalize}}.query
    total = q.count()

    if sort_by.startswith('-'):
        sort_by = getattr({{cookiecutter.module_name|capitalize}}, sort_by[1:]).desc()
    else:
        sort_by = getattr({{cookiecutter.module_name|capitalize}}, sort_by)

    q = q.order_by(sort_by).offset((page - 1) * limit).limit(limit)
    return success(
        results=[i.to_dict() for i in q],
        total=total
    )


@mod.route('/<int:{{cookiecutter.module_name|lower}}_id>/')
@swag_from({{cookiecutter.module_name|upper}}_BY_ID)
def {{cookiecutter.module_name|lower}}_by_id_view({{cookiecutter.module_name|lower}}_id):
    {{cookiecutter.module_name|lower}} = {{cookiecutter.module_name|capitalize}}.query.filter_by(id={{cookiecutter.module_name|lower}}_id).one()
    return success(**{{cookiecutter.module_name|lower}}.to_dict())


@mod.route('/', methods=['POST'])
@swag_from({{cookiecutter.module_name|upper}}_CREATE)
@use_kwargs(ADD_{{cookiecutter.module_name|upper}}_SCHEMA)
def add_{{cookiecutter.module_name|lower}}_view({{cookiecutter.module_name|lower}}_id=None, **kwargs):

    if {{cookiecutter.module_name|lower}}_id:
        i = {{cookiecutter.module_name|capitalize}}.query.filter_by(id={{cookiecutter.module_name|lower}}_id).one()
        setattrs(i, **kwargs, updated_at=datetime.utcnow())
    else:
        i = {{cookiecutter.module_name|capitalize}}(**kwargs)
        db.session.add(i)

    db.session.commit()

    return success(**i.to_dict())


@mod.route('/<int:{{cookiecutter.module_name|lower}}_id>/', methods=['PUT'])
@swag_from({{cookiecutter.module_name|upper}}_UPDATE)
@use_kwargs(UPDATE_{{cookiecutter.module_name|upper}}_SCHEMA)
def update_{{cookiecutter.module_name|lower}}_view({{cookiecutter.module_name|lower}}_id, **kwargs):
    return add_{{cookiecutter.module_name|lower}}_view({{cookiecutter.module_name|lower}}_id, **kwargs)


@mod.route('/<int:{{cookiecutter.module_name|lower}}_id>/', methods=['DELETE'])
@swag_from({{cookiecutter.module_name|upper}}_DELETE)
def delete_{{cookiecutter.module_name|lower}}_view({{cookiecutter.module_name|lower}}_id):
    i = {{cookiecutter.module_name|capitalize}}.query.filter_by(id={{cookiecutter.module_name|lower}}_id).one()
    db.session.delete(i)
    db.session.commit()
    return success(**i.to_dict())
