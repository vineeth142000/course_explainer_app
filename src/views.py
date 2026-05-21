from flask import render_template, abort
from models import courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    if course_id < 1 or course_id > len(courses):
        abort(404)
    return render_template('course.html', course=courses[course_id - 1])