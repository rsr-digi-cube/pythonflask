from myproject import create_app
from flask_swagger_ui import get_swaggerui_blueprint
from myproject.views import api_bp
SWAGGER_URL='/documentation'
API_URL='/static/documentation.json'
swaggerui_blueprint=get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app = create_app()
app.register_blueprint(api_bp,url_prefix='/admin')
app.register_blueprint(swaggerui_blueprint, url_prefix='/documentation')
try:
    if __name__ == '__main__':
        app.run(debug=True,host='192.168.43.238',port=8080)
except Exception as e:
    print(str(e))
    exit()
