from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app =Flask(__name__)


class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this mwill allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

#create table schema in the database, Requires application context
# with app.app_context():
#     db.create_all()


# create record
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J.K Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.title =="Harry Potter"))   # .order_by(Book.title))
    all_books= result.scalar()   # result.scalars()
    print(all_books)

with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    book_to_update.title="Harry Potter Story"
    db.session.commit()


# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
