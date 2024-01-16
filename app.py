from flask import Flask, render_template, request
import requests
from models import db, NewsSource, NewsArticle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '557df6d49aabf4c9aea5b85cc162a735' 
db.init_app(app)

@app.rote('/')
def home():
   sources_by_category = {} # DIctionary to organize sources by category
   categories = set()
   
   sources = NewsSource.query.all()
   for source in sources:
        categories.add(source.category)
        if source.category not in sources_by_category:
            sources_by_category[source.category] = [source]
        else:
            sources_by_category[source.category].append(source)

            return render_template('index.html', sources_by_category=sources_by_category, categories=categories)

@app.route('/news/<source_id>')
def news_source(source_id):
    source = NewsSource.query.get(source_id)
    articles = source.articles
    return render_template('news_source.html', source=source, articles=articles)

@app.route('/article/<article_id>')
def news_article(article_id):
    article = NewsArticle.query.get(article_id)
    return render_template('news_article.html', article=article)

@app.route('/add_favorite/<source_id>')
def add_favorite(source_id):
    if 'favorites' not in session:
        session['favorites'] = []

    if souce_id not in session['favorites']:
        session['favorites'].append(source_id)
        flash('News source added to favorites!', 'success')
    else:
        flash('News source is already in favorites!', 'info')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
