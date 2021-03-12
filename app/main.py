from app import db, app
import views
#
from models import Author, Book
import datetime


if __name__ == '__main__':
    db.create_all()
    app.run()

    # Добавляємо об'єкти в базу
    # author = Author(name='Bob Bismark', date_of_birth=datetime.date(year=1980, month=2, day=1))
    # db.session.add(author)
    # db.session.commit()
    # book1 = Book(name='First Book', author_id=author.id)
    # book2 = Book(name='Second Book', author_id=author.id)
    # book3 = Book(name='Python Book', author_id=author.id)
    # db.session.add_all([book1, book2, book3])
    # db.session.commit()
