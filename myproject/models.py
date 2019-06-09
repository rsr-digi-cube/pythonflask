from . import db
class Author(db.Document):
    email = db.StringField()
    password=db.StringField()
class Book(db.Document):
    title = db.StringField()
    author = db.DocumentField(Author)
    year = db.IntField();
