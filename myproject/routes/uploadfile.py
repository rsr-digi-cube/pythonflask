from flask import Blueprint,request
from flask_restful import Resource, Api, reqparse
from ..models import Author
import json
import werkzeug
from mongoalchemy.session import Session
import time
import tinys3
import os
AWS_ACCESS_KEY=""
AWS_SECRET_KEY=""
BUCKET_NAME=""
class uploadFile(Resource):
        def post(self):
            try:
                parse = reqparse.RequestParser()
                parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
                args = parse.parse_args()
                file = args['file']
                millis = int(round(time.time() * 1000))
                filename=str(millis)+".jpg"
                filepath="./uploads/"+filename
                file.save(filepath)
                conn = tinys3.Connection(AWS_ACCESS_KEY, AWS_SECRET_KEY, tls=True)
                f = open(filepath, 'rb')
                uploadFile = conn.upload(filename, f, BUCKET_NAME)
                os.remove(filepath)
                return {"message":"Successfully uploaded"},200
            except Exception as e:
                return {"message":str(e)},400
