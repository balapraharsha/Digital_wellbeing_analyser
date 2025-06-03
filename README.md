
# 📱 Digital Wellbeing Analyzer

A Streamlit-based interactive web app that helps users explore their **digital wellbeing** by analyzing their daily data on screen time, app usage, sleep, productivity, and mood. The app also includes a **machine learning model** to predict mood based on daily habits.
An interactive Streamlit app to explore personal digital habits like screen time, mood, sleep, productivity, and app usage.

🔗 **Live Demo:** [Click here to open the app](https://mood-predictor-app.streamlit.app/)

---

## 🚀 Features

- 📊 **Summary Dashboard** with average stats for screen time, sleep, productivity, and mood  
- 📈 **Daily Trends** for screen time  
- 💼 **Sleep vs Productivity Analysis**, colored by mood  
- 🎮 **App Usage Breakdown** (Social Media, Work, Entertainment)  
- 😊 **Mood Score Distribution**  
- 📅 **Day-wise Productivity Analysis**  
- 🤖 **Mood Prediction Model** based on input features like sleep, productivity, and app usage  
- 🌐 **Responsive Layout** that works on both desktop and mobile

---

## 🧠 Technologies Used

- **Frontend:** Streamlit  
- **Data Analysis & Visualization:** Pandas, Seaborn, Matplotlib  
- **Machine Learning:** Scikit-learn (Random Forest Classifier), Joblib  

---

## 📂 Project Structure

```
Digital_wellbeing_analyser/
│
├── app.py                            # Main Streamlit app
├── ml_predictor.py                   # Script to train and save the ML model
├── mood_predictor_model.pkl          # Saved ML model
├── digital_wellbeing_cleaned.csv     # Cleaned dataset
├── requirements.txt                  # List of dependencies
├── README.md                         # Project documentation
└── notebooks/                        # Colab notebooks for data cleaning, EDA, etc.
    └── data_cleaning.ipynb
    └── eda.ipynb
    └── digital_wellbeing_365_days.csv
```

---

## 🧪 How to Run Locally

1. **Clone the Repository**  
```
git clone https://github.com/your-username/digital-wellbeing-analyzer.git
cd digital-wellbeing-analyzer
```

2. **Install Dependencies**  
```
pip install -r requirements.txt
```

3. **Run the App**  
```
streamlit run app.py
```

---

## 💡 Model Details

- The ML model uses the following features to predict **mood (1–5)**:
  - Sleep Hours  
  - Productivity (1–5)  
  - Social Media (min)  
  - Work Apps (min)  
  - Entertainment (min)

---

## 🛠️ To Do (Optional Enhancements)

- [ ] Add login/user-based data upload
- [ ] Improve mobile UI responsiveness
- [ ] Add insights or recommendations
- [ ] Deploy on Streamlit Cloud / Hugging Face Spaces

---

## 👨‍💻 Author

**Mannepalli Bala Praharsha**  
Built as part of personal productivity & AI/ML learning journey.  
Feel free to ⭐ the repo if you found it helpful!

---
