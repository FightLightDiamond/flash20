from flask import request, jsonify
from library.marshallow import StudentSchema
import json
from library.model import Students

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


def get_all_students_service():
    students = Students.query.all()
    if students:
        return students_schema.jsonify(students)
    else:
        return jsonify({"message": "Not found students!"}), 404
