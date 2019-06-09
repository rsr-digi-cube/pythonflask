from flask import Blueprint,request
from flask_restful import Resource, Api, reqparse
from ..models import Author
import json
from mongoalchemy.session import Session
UPLOAD_FOLDER = '../uploads'
class login(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, required=True, help="Name cannot be blank!")
            parser.add_argument('password', type=str)
            author=Author(email=parser.parse_args()['email'],password=parser.parse_args()['password'])
            data = author.save()

            dataTosend=Author.query
            return dataTosend
        except Exception as e:
            return str(e)
