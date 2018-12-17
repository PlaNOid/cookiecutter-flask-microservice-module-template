list_view = dict(
    summary='List of {{cookiecutter.module_name|capitalize}}s',
    tags=['{{cookiecutter.module_name|upper}}S'],
    responses={
        '200': dict(
            description="""
            {
                "data": {
                    "results": [
                        {
                            "id": 1,
                            "created_at": "2018-10-10",
                            "updated_at": "2018-10-10",
                        }
                    ],
                    "total": 1
                }
            }
            """
        )
    }
)
{{cookiecutter.module_name|lower}}_by_id_view = dict(
    summary='{{cookiecutter.module_name|capitalize}} by id',
    tags=['{{cookiecutter.module_name|upper}}S'],
    responses={
        '200': dict(
            description="""
            {
                "data": {
                    "id": 1,
                    "created_at": "2018-10-10",
                    "updated_at": "2018-10-10",
                }
            }
            """
        )
    }
)

add_{{cookiecutter.module_name|lower}}_view = dict(
    summary='Create {{cookiecutter.module_name|capitalize}}',
    tags=['{{cookiecutter.module_name|upper}}S'],
    responses={
        '200': dict(
            description="""
            {
                "data": {
                    "id": 1,
                    "created_at": "2018-10-10",
                    "updated_at": "2018-10-10",
                }
            }
            """
        )
    },
)

update_{{cookiecutter.module_name|lower}}_view = dict(
    summary='Update {{cookiecutter.module_name|capitalize}}',
    tags=['{{cookiecutter.module_name|upper}}S'],
    responses={
        '200': dict(
            description="""
            {
                "data": {
                    "id": 1,
                    "created_at": "2018-10-10",
                    "updated_at": "2018-10-10",
                }
            }
            """
        )
    },
)

delete_{{cookiecutter.module_name|lower}}_view = dict(
    summary='Delete {{cookiecutter.module_name|capitalize}}',
    tags=['{{cookiecutter.module_name|upper}}S'],
    responses={
        '200': dict(
            description="""
            {
                "data": {
                    "id": 1,
                    "created_at": "2018-10-10",
                    "updated_at": "2018-10-10",
                }
            }
            """
        )
    }
)
