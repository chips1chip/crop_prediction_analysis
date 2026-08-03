# 🌱 Crop Prediction Analysis

A machine learning-based web application developed using **Python** and **Streamlit** that recommends the most suitable crop based on soil nutrients and environmental conditions. The application uses a **Random Forest Classifier** trained on agricultural data to provide accurate crop recommendations.

---

## 📌 Features

- Predict the most suitable crop for cultivation
- Interactive and user-friendly Streamlit interface
- Fast and accurate predictions
- Uses soil and weather parameters
- Real-time crop recommendation

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```
Crop_Prediction_Analysis/
│── front.py              # Streamlit application
│── crop.py               # Model training script
│── crop_model.pkl        # Trained Random Forest model
│── cpdata.csv            # Dataset
│── README.md
```

---

## 📊 Input Parameters

The model predicts the best crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

---

## 🤖 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Problem Type:** Multi-class Classification
- **Training Dataset:** Crop Recommendation Dataset

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Crop_Prediction_Analysis.git
```

Navigate to the project folder:

```bash
cd Crop_Prediction_Analysis
```

Install the required libraries:

```bash
pip install streamlit pandas numpy scikit-learn
```

---

## ▶️ Run the Application

```bash
streamlit run front.py
```

---

## 📖 How to Use

1. Launch the Streamlit application.
2. Enter the required soil nutrient values.
3. Provide environmental conditions.
4. Click **Predict**.
5. View the recommended crop.

---

## 📈 Future Improvements

- Fertilizer recommendation
- Crop yield prediction
- Weather API integration
- Disease prediction
- Soil quality analysis
- Cloud deployment

---

## 📸 Application Preview

*Add screenshots of your Streamlit application here.*

---

## 👩‍💻 Author

**Anjali Negi**

B.Tech Computer Science & Engineering

---

## 📄 License

This project is intended for educational and learning purposes.
