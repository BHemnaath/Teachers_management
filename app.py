'''import flask
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)


@app.route('/')
def index():
    with open('teachers.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        teachers = list(reader)

    return render_template('index.html', teachers=teachers)


@app.route('/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        full_name = request.form['full_name']
        age = int(request.form['age'])
        dob = request.form['dob']
        num_classes = int(request.form['num_classes'])

        with open('teachers.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['full_name', 'age', 'dob', 'num_classes'])
            writer.writerow({'full_name': full_name, 'age': age, 'dob': dob, 'num_classes': num_classes})

        return redirect(url_for('index'))

    return render_template('add_teacher.html')


@app.route('/filter', methods=['GET', 'POST'])
def filter_teachers():
    if request.method == 'POST':
        filter_criteria = request.form['filter_criteria']
        filter_value = request.form['filter_value']

        with open('teachers.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            teachers = list(reader)

        filtered_teachers = [teacher for teacher in teachers if teacher[filter_criteria] == filter_value]

        return render_template('filter_teachers.html', teachers=filtered_teachers)

    return render_template('filter_criteria.html')


if __name__ == '__main__':
    app.run(debug=True)'''

import flask
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route("/")  # Changed to '/' to make index as the homepage
def display_teachers():
    with open("teacher_data.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        teachers = list(reader)

    return render_template("index.html", teachers=teachers)

@app.route("/add_teacher", methods=["GET", "POST"])
def add_new_teacher():
    if request.method == "POST":
        teacher_name = request.form["full_name"]
        teacher_age = int(request.form["age"])
        teacher_dob = request.form["dob"]
        teacher_classes = int(request.form["num_classes"])

        with open("teacher_data.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["full_name", "age", "dob", "num_classes"])
            writer.writerow({"full_name": teacher_name, "age": teacher_age, "dob": teacher_dob, "num_classes": teacher_classes})

        return redirect(url_for("display_teachers"))

    return render_template("add_teacher.html")

@app.route("/filter_teachers", methods=["GET", "POST"])
def filter_teachers_by_criteria():
    if request.method == "POST":
        filter_field = request.form["filter_criteria"]
        filter_value = request.form["filter_value"]

        with open("teacher_data.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            teachers = list(reader)

        filtered_teachers = [teacher for teacher in teachers if teacher[filter_field] == filter_value]

        return render_template("filter_teachers.html", teachers=filtered_teachers)

    return render_template("filter_criteria.html")

if __name__ == "__main__":
    app.run(debug=True)