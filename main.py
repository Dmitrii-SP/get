import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator

def main():
    # Grab the config, add a view, and make a WSGI app
    config = Configurator()
    config.include('pyramid_chameleon')
    config.scan("views")
    app = config.make_wsgi_app()
    return app


if __name__ == '__main__':
    # When run from command line, launch a WSGI server and app
    app = main()
    server = make_server(os.getenv('IP', '0.0.0.0'), int(os.getenv('PORT', 5000)), app)
    server.serve_forever()