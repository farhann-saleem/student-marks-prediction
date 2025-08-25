import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load trained model (assuming you saved it as 'model.pkl')
model = pickle.load(open("student_marks_pred_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        study_hours = float(request.form["study_hours"])
        courses = int(request.form["courses"])

        # Prediction
        features = np.array([[study_hours, courses]])
        prediction = model.predict(features)[0]

        return render_template("index.html",
                               prediction_text=f"🎯 Predicted Marks: {round(prediction, 2)}")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
