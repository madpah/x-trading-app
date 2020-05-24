import connexion
from flask_cors import CORS

from .domain.config import Config

config = Config().get()

app = connexion.FlaskApp(__name__, specification_dir='./swagger/', debug=config.getboolean('app', 'debug'))
app.add_api('swagger.yml')
cors = CORS(app=app.app, resources={r"/*": {"origins": config.get('app', 'cors_origins').split(',')}})

# Expose the Flask App so WSGI server can access it
flask_app = app.app

if __name__ == 'main':
    # If just running manually outside of WSGI server, run the app
    app.run(port=config.getint('app', 'port'))