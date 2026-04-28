# 📚 AI Study Planner (Machine Learning Project)

## 🔍 Overview

This project predicts how many hours a student should study based on:

* Subject
* Score
* Days left for exam

It uses a **Decision Tree Regressor** to make predictions.

---

## ⚙️ Features

* Predicts daily study hours
* Assigns priority (High / Medium / Low)
* Visualizes decision tree
* Shows relationship between score and study hours

---

## 🧠 Machine Learning Model

* Algorithm: Decision Tree Regressor
* Input Features:

  * Subject
  * Difficulty (default)
  * Score
  * Hours Studied (default)
  * Days Left
* Output:

  * Recommended Study Hours

---

## 📊 Visualization

* Decision Tree Diagram
* Score vs Study Hours Graph

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## ⚠️ Note

Some features like difficulty and hours studied are set to default values for simplicity.

---

## 💡 Future Improvements

* Take difficulty as user input
* Improve dataset size
* Convert into web app using Streamlit
