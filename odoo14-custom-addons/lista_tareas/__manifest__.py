# -*- coding: utf-8 -*-
{
    'name': "MyList",

    'summary': """
    Haz tu Lista de tareas""",

    'description': """
    Este es un modulo que te permite crear tus lista de tareas con sus categorias
    """,

    'author': "Alejandro González Hermoso",
    'website': "https://github.com/DiyMaker?tab=repositories",
    #Indicamos que es una aplicación
    'application': True,

    # En la siguiente URL se indica que categorias pueden usarse
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoria Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de modulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del modulo "base"
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        #Este primero indica la politica de acceso del modulo
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/views.xml',
    ]
}
