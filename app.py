import streamlit as st
import pandas as pd
import numpy as np
import joblib  
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Digital Wellbeing Analyzer", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("C:\\Users\\balap\\Desktop\\VS CODE\\Digital_wellbeing_analyser\\digital_wellbeing_cleaned.csv", parse_dates=["Date"])
    return df

df = load_data()

st.title("📱 Digital Wellbeing Analyzer")
st.markdown("Gain insights into your **digital habits**: app usage, mood, sleep, and productivity over time.")

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
selected_day = st.sidebar.multiselect("Select Day(s):", options=df["Day"].unique(), default=df["Day"].unique())
filtered_df = df[df["Day"].isin(selected_day)]

# Section 1: Overview
st.subheader("📊 Summary Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg. Screen Time (hrs)", round(filtered_df["Total Screen Time (min)"].mean() / 60, 2))
col2.metric("Avg. Sleep (hrs)", round(filtered_df["Sleep Hours"].mean(), 2))
col3.metric("Avg. Productivity", round(filtered_df["Productivity (1-5)"].mean(), 2))
col4.metric("Avg. Mood", round(filtered_df["Mood (1-5)"].mean(), 2))

# Section 2: Screen Time Trend
st.subheader("📱 Screen Time Over Time")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered_df, x="Date", y="Total Screen Time (min)", ax=ax1, label="Screen Time", color="orange")
ax1.set_title("Daily Screen Time Trend")
ax1.set_ylabel("Minutes")
ax1.set_xlabel("")
st.pyplot(fig1)

# Section 3: Sleep vs. Productivity
st.subheader("😴 Sleep vs 💼 Productivity")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x="Sleep Hours",
    y="Productivity (1-5)",
    hue="Mood (1-5)",
    palette="coolwarm",
    ax=ax2
)
ax2.set_title("Impact of Sleep on Productivity (Colored by Mood)")
st.pyplot(fig2)

# Section 4: App Usage Breakdown
st.subheader("📱 App Usage Breakdown")
app_columns = ["Social Media (min)", "Work Apps (min)", "Entertainment (min)"]
avg_app_usage = filtered_df[app_columns].mean().sort_values(ascending=False)
st.bar_chart(avg_app_usage)

# Section 5: Mood Distribution
st.subheader("😊 Mood Score Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(filtered_df["Mood (1-5)"], bins=5, kde=True, color="skyblue", ax=ax3)
ax3.set_title("Mood Score Distribution (1=Low, 5=High)")
st.pyplot(fig3)

# Section 6: Productivity by Day
st.subheader("📅 Average Productivity by Day")
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_productivity = (
    filtered_df.groupby("Day")["Productivity (1-5)"]
    .mean()
    .reindex(day_order)
)
fig4, ax4 = plt.subplots()
day_productivity.plot(kind="bar", color="green", ax=ax4)
ax4.set_title("Average Productivity by Day")
st.pyplot(fig4)

# Mood Prediction Section
st.subheader("🔮 Predict Your Mood")
st.markdown("Adjust your daily inputs to see the predicted mood score (1-5):")

sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0, 0.5)
productivity = st.slider("Productivity (1-5)", 1, 5, 3)
social = st.slider("Social Media (min)", 0, 300, 60)
work = st.slider("Work Apps (min)", 0, 300, 90)
entertainment = st.slider("Entertainment (min)", 0, 300, 60)

# ✅ Add total screen time to match training features
total_screen_time = social + work + entertainment
input_data = np.array([[sleep, productivity, social, work, entertainment, total_screen_time]])

# Load model and predict
model = joblib.load("mood_predictor_model.pkl")
mood_pred = model.predict(input_data)[0]

st.success(f"🎯 Predicted Mood Score: **{round(mood_pred, 2)}**")


# Footer
st.markdown("---")
st.markdown("🔍 Built by Mannepalli Bala Praharsha using Streamlit | Project: Digital Wellbeing Analyzer")
