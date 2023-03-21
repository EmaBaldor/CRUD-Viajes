from flask import Flask
from config import config

#rutas
from routes import viajes

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(viajes.main,url_prefix='/')
    
    #Error pagina no encontrada
    app.register_error_handler(404,page_not_found)
    app.run()
