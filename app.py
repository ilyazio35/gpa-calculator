from flask import Flask, render_template, request
from calculator import calculate_gpa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        grades = request.form.getlist('grade[]')
        credits = request.form.getlist('credit[]')

        if len(grades) != len(credits):
            result = "Error: Mismatched number of grades and credits."
        else:
            result = calculate_gpa(grades, credits)

    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run()
