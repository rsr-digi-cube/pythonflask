from flask import Blueprint,request
from flask_restful import Resource, Api, reqparse
from ..models import Author
import json
import werkzeug
from mongoalchemy.session import Session
import time
import boto.ses
AWS_ACCESS_KEY=""
AWS_SECRET_KEY=""
class Register(Resource):
        def post(self):
            try:
                connection = boto.ses.connect_to_region(
                    'us-west-2',
                    aws_access_key_id=AWS_ACCESS_KEY,
                    aws_secret_access_key=AWS_SECRET_KEY
                )

                parser = reqparse.RequestParser()
                parser.add_argument('email', type=str, required=True, help="Name cannot be blank!")


                return connection.send_email(
                    "craftatcom@gmail.com",
                    "Testing",
                    None,
                    parser.parse_args()['email'],
                    format="html",
                    text_body="demo",
                    html_body="demo"
                )

                return {"message":"Successfully send email"},200
            except Exception as e:
                return str(e)
