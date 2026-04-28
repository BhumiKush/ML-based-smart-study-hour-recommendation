import streamlit as st
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("study_dataset.csv")

# ==============================
# TRAIN MODEL
# ==============================
le_subject = LabelEncoder()
le_difficulty = LabelEncoder()

df["Subject"] = le_subject.fit_transform(df["Subject"])
df["Difficulty"] = le_difficulty.fit_transform(df["Difficulty"])

X = df[["Subject", "Difficulty", "Score", "Hours_Studied", "Days_Left"]]
y = df["Recommended_Hours"]

model = DecisionTreeRegressor()
model.fit(X, y)

# ==============================
# UI DESIGN
# ==============================
st.title("📚 Smart Study Planner")

st.write("Enter your subjects and get a personalized study plan.")

num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=10, step=1)

inputs = []

for i in range(int(num_subjects)):
    st.subheader(f"Subject {i+1}")
    
    subject = st.text_input(f"Subject Name {i+1}", key=f"sub{i}")
    score = st.number_input(f"Score {i+1}", min_value=0, max_value=100, key=f"score{i}")
    days_left = st.number_input(f"Days Left {i+1}", min_value=1, key=f"days{i}")
    
    inputs.append({
        "Subject": subject,
        "Score": score,
        "Days_Left": days_left
    })

# ==============================
# BUTTON
# ==============================
if st.button("Generate Study Plan"):

    multi_df = pd.DataFrame(inputs)

    # Handle subject encoding
    encoded_subjects = []
    valid_subjects = list(le_subject.classes_)

    for sub in multi_df["Subject"]:
        if sub in valid_subjects:
            encoded_subjects.append(le_subject.transform([sub])[0])
        else:
            encoded_subjects.append(int(df["Subject"].mean()))

    multi_df["Subject_Original"] = multi_df["Subject"]
    multi_df["Subject"] = encoded_subjects

    # Default values
    multi_df["Difficulty"] = 1
    multi_df["Hours_Studied"] = 1

    # Prediction
    features = ["Subject", "Difficulty", "Score", "Hours_Studied", "Days_Left"]
    multi_df["Recommended_Hours"] = model.predict(multi_df[features])

    # Priority logic
    def get_priority(days):
        if days <= 3:
            return "High 🔴"
        elif days <= 7:
            return "Medium 🟡"
        else:
            return "Low 🟢"

    multi_df["Priority"] = multi_df["Days_Left"].apply(get_priority)

    # Round hours
    def round_hours(hours):
        if hours < 1:
            return 1
        elif hours < 2:
            return 1.5
        elif hours < 3:
            return 2
        elif hours < 4:
            return 3
        else:
            return 4

    multi_df["Daily_Hours"] = multi_df["Recommended_Hours"].apply(round_hours)

    # OUTPUT
    st.subheader("📅 Your Study Plan")

    for _, row in multi_df.iterrows():
        st.markdown(f"### 📘 {row['Subject_Original']}")
        st.write(f"Priority: {row['Priority']}")
        st.write(f"Study Time: {row['Daily_Hours']} hrs/day")
        st.write("---")