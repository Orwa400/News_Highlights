from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy

class NewsSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    articles = db.relationship('NewsArticle', backref='source', lazy=True)
    