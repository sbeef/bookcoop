from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String())
  author = db.Column(db.String())

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __repr__(self):
    return '<Book %r>' % self.title

