from library import db


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    birthday = db.Column(db.Date)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(10))

    # borrows = db.relationship('Borrows', backref='borrow', lazy=True)

    def __init__(self, name, birthday, gender, class_name):
        self.name = name
        self.birthday = birthday
        self.gender = gender
        self.class_name = class_name

    def __repr__(self):
        return '<Students %r>' % self.name

#
# class Books(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#     page_count = db.Column(db.Integer)
#     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
#
#     def __init__(self, name, page_count, author_id, category_id):
#         self.name = name
#         self.page_count = page_count
#         self.author_id = author_id
#         self.category_id = category_id
#
#     def __repr__(self):
#         return '<Books %r>' % self.name
#
#
# class Borrows(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
#     student_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
#     borrow_date = db.Column(db.Date, nullable=True)
#     return_date = db.Column(db.Date, nullable=True)
#
#     # student = db.relationship('Students', backref='borrow', lazy=True)
#
#     def __init__(self, book_id, student_id, borrow_date, return_date):
#         self.book_id = book_id
#         self.student_id = student_id
#         self.borrow_date = borrow_date
#         self.return_date = return_date
#
#     def __repr__(self):
#         return '<Books %r>' % self.name
#
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#
#     book = db.relationship('Books', backref='book', lazy=True)
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Author(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#
#     book = db.relationship('Books', backref='book', lazy=True)
#
#     def __init__(self, name):
#         self.name = name

