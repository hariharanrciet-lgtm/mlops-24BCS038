from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load("student_model.joblib")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Predictor</title>
</head>
<body>
    <h1>Student Result Predictor</h1>
    <form method="POST">
        <label>Study Hours:</label>
        <input type="number" name="hours" min="0" max="24" required>
        <br><br>

        <label>Attendance (%):</label>
        <input type="number" name="attendance" min="0" max="100" required>
        <br><br>

        <label>Internal Marks:</label>
        <input type="number" name="marks" min="0" max="100" required>
        <br><br>

        <button type="submit">Predict Result</button>
    </form>
    {% if result %}
        <h2>Predicted Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        marks = float(request.form["marks"])

        result = model.predict([[hours, attendance, marks]])[0]

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
