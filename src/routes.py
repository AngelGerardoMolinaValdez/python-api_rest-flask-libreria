from controllers import *
from flask import Flask

def initialize_routes(app: Flask):
    app.add_url_rule(
        '/products',
        view_func=handle_products,
        methods=['GET', 'POST']
    )
    app.add_url_rule(
        '/products/<string:id>',
        view_func=handle_product,
        methods=['GET', 'PUT', 'DELETE']
    )

    app.add_url_rule(
        '/categories',
        view_func=handle_categories,
        methods=['GET', 'POST']
    )

    app.add_url_rule(
        '/categories/<string:id>',
        view_func=handle_category,
        methods=['GET', 'PUT', 'DELETE']
    )
