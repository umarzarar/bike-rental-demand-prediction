
# 🚲 Bike Rental Demand Prediction

A machine learning project that predicts hourly bike rental demand using historical rental data, weather conditions, and calendar-related features. The project demonstrates an end-to-end ML workflow, from data preprocessing and exploratory data analysis to model training and deployment through an interactive Streamlit application.

Developed as part of my AI/ML learning journey with **Big Brains**.

## 🌟 Project Overview

Bike rental services need to estimate demand to manage bike availability and plan operations efficiently.

This project uses a **Linear Regression** model to predict the number of bike rentals based on selected input conditions. The deployed application allows users to explore different scenarios and observe the model's predictions.

## 🎯 Objectives

- Understand a real-world demand prediction problem.
- Perform data cleaning and exploratory data analysis (EDA).
- Prepare features for machine learning.
- Train and evaluate a regression model.
- Build an interactive Streamlit application.
- Test predictions using preset and customized scenarios.

## 📊 Dataset

**Dataset:** UCI Bike Sharing Dataset  
**Source:** Kaggle — Bike Rental Dataset

The dataset contains historical bike-sharing records with information about time, weather, and rental counts.

### Target Variable

| Variable | Description |
|---|---|
| `count` | Total number of bike rentals; the value predicted by the model |

### Features

The dataset includes features such as:

- `year` — year indicator
- `hour` — hour of the day
- `season` — season of the year
- `holiday` — whether the day is a holiday
- `workingday` — whether the day is a working day
- `weather` — weather category
- `temp` — temperature
- `atemp` — perceived temperature
- `humidity` — humidity level
- `windspeed` — wind speed

Additional engineered and encoded features are used during model preparation.

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing

- Loaded and inspected the dataset.
- Corrected the semicolon-separated CSV format.
- Checked data structure and prepared features.
- Applied one-hot encoding to categorical variables.
- Created cyclical hour features using sine and cosine transformations.

### 2. Exploratory Data Analysis

Explored the relationship between rental demand and relevant features, including time, weather, and calendar conditions.

The analysis helped identify patterns in hourly demand and understand how different conditions relate to bike rentals.

### 3. Feature Engineering

The hour of the day is cyclical: hour 23 is close to hour 0.

To represent this relationship, the following features were created:

- `hour_sin`
- `hour_cos`

This helps the model represent the circular nature of time.

### 4. Model Training

| Component | Details |
|---|---|
| Problem type | Regression |
| Algorithm | Linear Regression |
| Target | `count` |
| Evaluation | MAE, MSE, RMSE, and R² |

The model was trained using prepared features to estimate bike rental demand.

### 5. Model Evaluation

The model was evaluated using common regression metrics:

| Metric | Purpose |
|---|---|
| MAE | Average absolute prediction error |
| MSE | Average squared prediction error |
| RMSE | Error expressed in the target's units |
| R² | Measures how much target variation is explained by the model |

> **Note:** Add your actual evaluation results here after confirming them from your final training notebook or report.

## 🖥️ Streamlit Web Application

The project includes an interactive web application called **Bike Demand AI**.

Users can adjust input conditions and generate bike rental demand predictions.

### Application Features

- Interactive prediction interface
- Four preset test scenarios
- Quick testing across different input conditions
- Customizable input values
- Real-time prediction display
- Simple interface for exploring model behavior

### 🧪 Preset Test Scenarios

Four preset scenarios are included to make testing faster and easier.

Users can select a scenario to populate the input fields and generate a prediction. They can also change the inputs themselves to experiment with different combinations of conditions.

These scenarios are intended for quick exploration and do not replace formal model evaluation.

## 🛠️ Technologies Used

- **Python** — programming language
- **Pandas** — data manipulation
- **NumPy** — numerical computing
- **Matplotlib** — data visualization
- **Scikit-learn** — machine learning and evaluation
- **Joblib** — saving and loading model artifacts
- **Streamlit** — interactive web application
- **Jupyter Notebook / Google Colab** — development and experimentation
- **Git & GitHub** — version control and project hosting

## 📁 Project Structure

```text
bike-rental-demand-prediction/
│
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies
├── bike_demand_model.pkl     # Trained ML model
├── model_features.pkl        # Model feature information
│
├── notebooks/                # Data analysis and model development
│
├── README.md                 # Project documentation
└── .gitignore                # Files excluded from Git
```

*Update this structure if your actual repository uses different filenames or folders.*

## 🚀 Run Locally

### Prerequisites

- Python installed
- Git installed
- The project repository cloned to your computer

### 1. Clone the Repository

```bash
git clone https://github.com/umarzarar/bike-rental-demand-prediction.git
```

### 2. Navigate to the Project

```bash
cd bike-rental-demand-prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate
```

### 4. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

> Ensure that the trained model and feature files are present in the expected locations before running the application.

## 📈 Example Use Case

A bike-sharing operator wants to estimate hourly rental demand under different conditions.

The user can:

1. Select one of the four preset scenarios or customize the inputs.
2. Enter the relevant time, weather, and calendar conditions.
3. Generate a prediction.
4. Compare the predicted demand across scenarios.

This demonstrates how a regression model can be integrated into an interactive application for exploring demand estimates.

## 🔮 Future Improvements

- Experiment with additional regression algorithms.
- Compare models using consistent evaluation metrics.
- Improve prediction accuracy through feature selection and tuning.
- Add visual comparisons between actual and predicted demand.
- Expand scenario testing and model validation.
- Explore time-series approaches for demand forecasting.
- Improve the deployment and user experience.

## 👨‍💻 Author

**Umar Zarar**  
BS Software Engineering Student | Aspiring AI/ML Engineer

- GitHub: [umarzarar](https://github.com/umarzarar)
- Project Repository: [Bike Rental Demand Prediction](https://github.com/umarzarar/bike-rental-demand-prediction)

## 🙌 Acknowledgment

This project was developed as part of my AI/ML learning journey with **Big Brains**.

Thanks to everyone supporting my learning and growth in machine learning.

---

⭐ If you find this project useful, feel free to explore the repository and try the application.
