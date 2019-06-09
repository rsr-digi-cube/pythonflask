from flask import Blueprint,request,jsonify
from flask_restful import Resource, Api, reqparse
from ..models import Author
import json
import werkzeug
from mongoalchemy.session import Session
import time
import boto.ses
import requests
class Requestpractice(Resource):
        def get(self):
            try:
                r=requests.get("http://3.122.33.203:8000/user/getCategory")
                return jsonify(r)
            except Exception as e:
                return {"message":str(e)},400
