import json
import os
import connexion
from flask_cors import CORS

connexion_app = connexion.FlaskApp(__name__, specification_dir='.')
connexion_app.add_api('openapi.yaml', validate_responses=True)

CORS(connexion_app.app)

if __name__ == '__main__':
    connexion_app.run(debug=True, host='0.0.0.0', port=8080)