from app import app, db
from flask import render_template, request, redirect, url_for
from models import Book, Author
from datetime import datetime

from flask_security import login_required


@app.route('/')
@login_required
def home():
    books_list = Book.query.all()
    authors_list = Author.query.all()
    return render_template('home.html', books=books_list, authors=authors_list)


@app.route('/create_author', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        name = request.form.get('name')
        date_of_birth_str = request.form.get('date_of_birth')

        try:
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
            author = Author(name=name, date_of_birth=date_of_birth)
            db.session.add(author)
            db.session.commit()
        except:
            print('Error. Something wrong...')
        return redirect(url_for('home'))

    return render_template('create_author.html')


@app.route('/book/<int:id>')
def book_detail(id):
    book = Book.query.filter(Book.id == id).first()
    return 'Book MOCK'


@app.route('/author/<int:id>')
def author_detail(id):
    author = Book.query.filter(Author.id == id).first()
    return 'Author MOCK'
