# ml_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib  # For saving the model

# Load cleaned data
df = pd.read_csv("C:\\Users\\balap\\Desktop\\VS CODE\\Digital_wellbeing_analyser\\digital_wellbeing_cleaned.csv", parse_dates=["Date"])

# Encode 'Weekend' as binary
df["Weekend"] = df["Weekend"].map({"Yes": 1, "No": 0})

# Select features and target
features = [
    "Sleep Hours",
    "Productivity (1-5)",
    "Social Media (min)",
    "Work Apps (min)",
    "Entertainment (min)",
    "Weekend"
]
target = "Mood (1-5)"


X = df[features]
y = df[target].astype(int)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
joblib.dump(model, "mood_predictor_model.pkl")
print("✅ Model trained and saved as 'mood_predictor_model.pkl'")
