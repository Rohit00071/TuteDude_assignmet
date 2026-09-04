from flask import Flask, request, render_template
from datetime import datetime



app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    day_of_week = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=["POST"])
def submit():
    form_data= dict(request.form)
    return f"Hello {form_data}"
if __name__ == "__main__":
    app.run(debug=True)
