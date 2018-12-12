from app.{{cookiecutter.module_name}}s.models import {{cookiecutter.module_name|capitalize}}
from tests.utils import unpack


module_name = {{cookiecutter.module_name|lower}}


def test_create_{{cookiecutter.module_name|lower}}(client):
    resp = client.post(
        endpoint=f'{module_name}s.add_{module_name}_view',
    )
    data = unpack(resp)

    assert 'id' in data
    assert {{cookiecutter.module_name|capitalize}}.query.filter_by(id=data['id']).one_or_none()


def test_{{cookiecutter.module_name|lower}}_list(client):
    resp = client.get(
        endpoint=f'{module_name}s.list_view',
    )
    data = unpack(resp)
    assert 'results' in data
    assert 'total' in data


def test_{{cookiecutter.module_name|lower}}_by_id(client):
    resp = client.get(
        endpoint=f'{module_name}s.{module_name}_by_id_view',
        {{cookiecutter.module_name|lower}}_id={{cookiecutter.module_name|capitalize}}.query.first().id,
    )
    data = unpack(resp)
    assert 'id' in data


def test_update_{{cookiecutter.module_name|lower}}(client):
    resp = client.put(
        endpoint=f'{module_name}s.update_{module_name}_view',
        {{cookiecutter.module_name|lower}}_id={{cookiecutter.module_name|capitalize}}.query.first().id,
    )
    data = unpack(resp)
    assert 'id' in data
    assert {{cookiecutter.module_name|capitalize}}.query.filter_by(id=data['id']).one().to_dict() == data


def test_delete_{{cookiecutter.module_name|lower}}(client):
    resp = client.delete(
        endpoint=f'{module_name}s.delete_{module_name}_view',
        {{cookiecutter.module_name|lower}}_id={{cookiecutter.module_name|capitalize}}.query.first().id,
    )
    data = unpack(resp)
    assert not {{cookiecutter.module_name|capitalize}}.query.filter_by(id=data['id']).one_or_none()
