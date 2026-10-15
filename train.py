import joblib
from sklearn.tree import DecisionTreeClassifier

X = [
    [1, 40, 10],
    [2, 50, 15],
    [3, 60, 20],
    [4, 70, 25],
    [5, 80, 30],
    [6, 90, 35],
]

y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "student_model.joblib")

print("Model trained successfully!")
