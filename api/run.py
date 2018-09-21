from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from app import api

MY_PREFIX = '/api'

class ReverseProxied(object):
    '''Wrap the application in this middleware and configure the
    front-end server to add these headers, to let you quietly bind
    this to a URL other than / and to an HTTP scheme that is
    different than what is used locally.

    :param app: the WSGI application
    '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = MY_PREFIX
        environ['SCRIPT_NAME'] = script_name
        path_info = environ['PATH_INFO']
        if path_info.startswith(script_name):
            environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = Flask(__name__)
app.url_map.strict_slashes = False
app.wsgi_app = ReverseProxied(app.wsgi_app)
app.register_blueprint(api)

#api.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)