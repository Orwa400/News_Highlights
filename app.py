from flask import Flask, render_template, request
import requests
from models import db, NewsSource, NewsArticle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.rote('/')
def home():
    sources = NewsSource.query.all()
    return render_template ('index.html', sources=sources)

@app.route('/news/<source_id>')
def news_source(source_id):
    source = NewsSource.query.get(source_id)
    articles = source.articles
    return render_template('news_source.html', source=source, articles=articles)

@app.route('/article/<article_id>')
def news_article(article_id):
    article = NewsArticle.query.get(article_id)
    return render_template('news_article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)
    