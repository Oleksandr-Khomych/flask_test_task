from app import app, db
from flask import render_template, request, redirect, url_for
from models import Book, Author
from datetime import datetime

from flask_security import login_required


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/book/')
def books():
    print(request.url_rule)
    q = request.args.get('q')
    if q:
        book_list = Book.query.filter(Book.name.contains(q)).all()
    else:
        book_list = Book.query.all()
    return render_template('books.html', books=book_list)


@app.route('/book/<int:id>/')
def book_detail(id):
    book = Book.query.filter(Book.id == id).first()
    author_name = db.session.query(Author.name).filter(Author.id == book.author_id).first()
    return render_template('book_detail.html', book=book, author_name=author_name[0])


@app.route('/author/')
def authors():
    q = request.args.get('q')
    if q:
        author_list = Author.query.filter(Author.name.contains(q)).all()
    else:
        author_list = Author.query.all()
    return render_template('authors.html', authors=author_list)


@app.route('/author/<int:id>')
def author_detail(id):
    author = Author.query.filter(Author.id == id).first()
    return render_template('author_detail.html', author=author)
