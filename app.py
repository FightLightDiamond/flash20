from flasgger import swag_from
from flask import jsonify
from werkzeug.utils import redirect

from src import create_app, Bookmark, db
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from src.database import User

app = create_app()


@app.get('/')
def index():
    name = User.query.first().name
    return "HELLO " + name


@app.get('/<short_url>')
@swag_from('./docs/short_url.yaml')
def redirect_to_url(short_url):
    bookmark = Bookmark.query.filter_by(short_url=short_url).first_or_404()

    if bookmark:
        bookmark.visits = bookmark.visits + 1
        db.session.commit()
        return redirect(bookmark.url)


@app.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
    return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND


@app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
def handle_500(e):
    return jsonify({'error': 'Something went wrong, we are working on it'}), HTTP_500_INTERNAL_SERVER_ERROR


if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=True, use_reloader=True)
