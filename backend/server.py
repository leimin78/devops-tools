from flask import Flask
from flask_cors import CORS
from app.api import api_blueprint

app = Flask(__name__)
CORS(app, supports_credentials=True)

#蓝本注册
app.register_blueprint(api_blueprint,url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)