from webargs import fields, validate
from app.common.schemas import FILTER_SCHEMA

FILTER_{{cookiecutter.module_upper_name}}S_SCHEMA = {
    **FILTER_SCHEMA
}

ADD_{{cookiecutter.module_upper_name}}_SCHEMA = {

}

UPDATE_{{cookiecutter.module_upper_name}}_SCHEMA = {
    **ADD_{{cookiecutter.module_upper_name}}_SCHEMA
}
