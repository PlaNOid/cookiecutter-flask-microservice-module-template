from datetime import datetime
from flask import Blueprint
from lib.utils import ujsonify, setattrs
from webargs.flaskparser import use_kwargs
from flask_builder import db

from .models import {{cookiecutter.model_name}}
from .schemas import FILTER_{{cookiecutter.module_upper_name}}S_SCHEMA, ADD_{{cookiecutter.module_upper_name}}_SCHEMA, UPDATE_{{cookiecutter.module_upper_name}}_SCHEMA

mod = Blueprint('{{cookiecutter.module_name}}s', __name__, url_prefix='/{{cookiecutter.module_name}}s')


@mod.route('/')
@use_kwargs(FILTER_{{cookiecutter.module_upper_name}}S_SCHEMA)
def list_view(page, limit, sort_by):
    q = {{cookiecutter.model_name}}.query
    total = q.count()

    if sort_by.startswith('-'):
        sort_by = getattr({{cookiecutter.model_name}}, sort_by[1:]).desc()
    else:
        sort_by = getattr({{cookiecutter.model_name}}, sort_by)

    q = q.order_by(sort_by).offset((page - 1) * limit).limit(limit)
    return ujsonify(
        results=[i.to_dict() for i in q],
        total=total
    )


@mod.route('/<int:{{cookiecutter.module_name}}_id>/')
def {{cookiecutter.module_name}}_by_id_view({{cookiecutter.module_name}}_id):
    {{cookiecutter.module_name}} = {{cookiecutter.model_name}}.query.filter_by(id={{cookiecutter.module_name}}_id).one()
    return ujsonify(**{{cookiecutter.module_name}}.to_dict())


@mod.route('/', methods=['POST'])
@use_kwargs(ADD_{{cookiecutter.module_upper_name}}_SCHEMA)
def add_{{cookiecutter.module_name}}_view({{cookiecutter.module_name}}_id=None, **kwargs):

    if {{cookiecutter.module_name}}_id:
        i = {{cookiecutter.model_name}}.query.filter_by(id={{cookiecutter.module_name}}_id).one()
        setattrs(i, **kwargs, updated_at=datetime.utcnow())
    else:
        i = {{cookiecutter.model_name}}(**kwargs)
        db.session.add(i)

    db.session.commit()

    return ujsonify(**i.to_dict())


@mod.route('/<int:{{cookiecutter.module_name}}_id>/', methods=['PUT'])
@use_kwargs(UPDATE_{{cookiecutter.module_upper_name}}_SCHEMA)
def update_{{cookiecutter.module_name}}_view({{cookiecutter.module_name}}_id, **kwargs):
    return add_{{cookiecutter.module_name}}_view({{cookiecutter.module_name}}_id, **kwargs)


@mod.route('/<int:{{cookiecutter.module_name}}_id>/', methods=['DELETE'])
def delete_{{cookiecutter.module_name}}_view({{cookiecutter.module_name}}_id):
    i = {{cookiecutter.model_name}}.query.filter_by(id={{cookiecutter.module_name}}_id).one()
    db.session.delete(i)
    db.session.commit()
    return 'ok'
