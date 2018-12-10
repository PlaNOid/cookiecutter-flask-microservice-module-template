{{cookiecutter.module_name|upper}}S_LIST = {
    'tags': [
        '{{cookiecutter.module_name|upper}}S'
    ],
    'parameters': [
        {
            'name': 'page',
            'in': 'query',
            'type': 'integer',
            'description': 'Page number',
            'default': 1,
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'description': 'Items per page',
            'default': 10,
        },
        {
            'name': 'sort_by',
            'in': 'query',
            'type': 'string',
            'description': 'Sorting attribute',
            'enum': [
                'id',
                'created_at',
                'updated_at',
            ],
            'default': 'id',
        },
    ],
    'definitions': {
        "{{cookiecutter.module_name|capitalize}}": {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'default': '123',
                },
                'created_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
                'updated_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
            },
        },
    },
    'responses': {
        '200': {
            'description': 'A list of {{cookiecutter.module_name|lower}}',
            'schema': {
                '$ref': '#/definitions/{{cookiecutter.module_name|capitalize}}'
            }
        }
    }
}

{{cookiecutter.module_name|upper}}_BY_ID = {
    'tags': [
        '{{cookiecutter.module_name|upper}}S'
    ],
    'parameters': [
        {
            'name': '{{cookiecutter.module_name|lower}}_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
        }
    ],
    'definitions': {
        '{{cookiecutter.module_name|capitalize}}': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'default': '123',
                },
                'created_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
                'updated_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
            },
        }
    },
    'responses': {
        '200': {
            'description': '{{cookiecutter.module_name|capitalize}} by id',
            'schema': {
                '$ref': '#/definitions/{{cookiecutter.module_name|capitalize}}'
            }
        },
    }
}

{{cookiecutter.module_name|upper}}_CREATE = {
    'tags': [
        '{{cookiecutter.module_name|upper}}S'
    ],
    'parameters': [

    ],
    'definitions': {
        '{{cookiecutter.module_name|capitalize}}': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'default': '123',
                },
                'created_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
                'updated_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
            },
        }
    },
    'responses': {
        '200': {
            'description': 'Create {{cookiecutter.module_name|lower}}',
            'schema': {
                '$ref': '#/definitions/{{cookiecutter.module_name|capitalize}}'
            }
        }
    }
}

{{cookiecutter.module_name|upper}}_UPDATE = {
    'tags': [
        '{{cookiecutter.module_name|upper}}S'
    ],
    'parameters': [
        {
            'name': '{{cookiecutter.module_name|lower}}_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
        }
    ],
    'definitions': {
        '{{cookiecutter.module_name|capitalize}}': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'default': '123',
                },
                'created_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
                'updated_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
            },
        }
    },
    'responses': {
        '200': {
            'description': 'Update {{cookiecutter.module_name|lower}}',
            'schema': {
                '$ref': '#/definitions/{{cookiecutter.module_name|capitalize}}'
            }
        }
    }
}

{{cookiecutter.module_name|upper}}_DELETE = {
    'tags': [
        '{{cookiecutter.module_name|upper}}S',
    ],
    'parameters': [
        {
            'name': '{{cookiecutter.module_name|lower}}_id',
            'in': 'path',
            'type': 'integer',
            'required': 'true',
        }
    ],
    'definitions': {
        '{{cookiecutter.module_name|capitalize}}': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'default': '123',
                },
                'created_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
                'updated_at': {
                    'type': 'string',
                    'default': '2018-12-06 08:36',
                },
            },
        }
    },
    'responses': {
        '200': {
            'description': 'Update {{cookiecutter.module_name|lower}}',
            'schema': {
                '$ref': '#/definitions/{{cookiecutter.module_name|capitalize}}'
            }
        }
    }
}
