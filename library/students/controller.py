from flask import Blueprint
from .service import get_all_students_service
students = Blueprint('students', __name__)


@students.get('/students')
def index():
    return get_all_students_service()

