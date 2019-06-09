from flask import Blueprint
from flask_restful import Api
from .routes.Login import login
from .routes.uploadfile import uploadFile
from .routes.Register import Register
from .routes.Requestpractice import Requestpractice
api_bp=Blueprint('api',__name__)
api=Api(api_bp)
api.add_resource(login,'/login')
api.add_resource(uploadFile,'/uploadFile')
api.add_resource(Register,'/register')
api.add_resource(Requestpractice,'/Requestpractice')
