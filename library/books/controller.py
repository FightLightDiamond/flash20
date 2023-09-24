from flask import Blueprint
# from .service import add_book_service, get_all_books_service
books = Blueprint('books', __name__)


# @books.get('/books')
# def index():
#     return get_all_books_service()
#
#
# @books.post('/books')
# def create():
#     # return 'add_book_service'
#     return add_book_service
