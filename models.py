from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy

class NewsSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    articles = db.relationship('NewsArticle', backref='source', lazy=True)

class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image =db.Column(db.String(100))
    created_at = db.Column(db.DataTime, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('news_source.id'), nullbale=False)

    
