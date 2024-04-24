from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), uniqu=True)
    author = db.Columm(db.String(100))
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"


@app.route("/")
def home():
    return "Hello, Flask!"

@app.rout('/books')
def get_books():
    books = Book.query.all()

    output = []
    for books in books:
        book_data = {'book': Book.name, 'author': Book.author, 'publisher': Book.publisher}
        output.append(book_data)
    return {"books": output}

@app.rout('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "author": book.author, "publisher": book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}