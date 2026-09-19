
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Bike Demand AI",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# LOAD TRAINED MODEL
# =====================================================
@st.cache_resource
def load_model():
    model = joblib.load("bike_demand_model.pkl")
    features = joblib.load("model_features.pkl")
    return model, features


model, model_features = load_model()


# =====================================================
# PRESET TEST SCENARIOS
# =====================================================
SCENARIOS = {
    "Custom (manual inputs)": {
        "year": 2012,
        "hour": 8,
        "season": 2,
        "weather": 1,
        "holiday": False,
        "workingday": True,
        "temp": 25.0,
        "atemp": 27.0,
        "humidity": 50,
        "windspeed": 10.0,
    },

    "Morning commute": {
        "year": 2012,
        "hour": 8,
        "season": 2,
        "weather": 1,
        "holiday": False,
        "workingday": True,
        "temp": 25.0,
        "atemp": 27.0,
        "humidity": 50,
        "windspeed": 10.0,
    },

    "Rainy day": {
        "year": 2012,
        "hour": 14,
        "season": 3,
        "weather": 3,
        "holiday": False,
        "workingday": True,
        "temp": 20.0,
        "atemp": 21.0,
        "humidity": 85,
        "windspeed": 15.0,
    },

    "Weekend afternoon": {
        "year": 2012,
        "hour": 15,
        "season": 2,
        "weather": 1,
        "holiday": False,
        "workingday": False,
        "temp": 28.0,
        "atemp": 30.0,
        "humidity": 45,
        "windspeed": 8.0,
    },

    "Late night": {
        "year": 2012,
        "hour": 23,
        "season": 4,
        "weather": 1,
        "holiday": False,
        "workingday": False,
        "temp": 10.0,
        "atemp": 9.0,
        "humidity": 65,
        "windspeed": 5.0,
    },
}


def apply_scenario():
    """Fill the input widgets using the selected preset."""
    selected = st.session_state["scenario"]
    values = SCENARIOS[selected]

    for key, value in values.items():
        st.session_state[key] = value


# Initialize widget values before creating widgets
default_values = SCENARIOS["Custom (manual inputs)"]

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

if "scenario" not in st.session_state:
    st.session_state["scenario"] = "Custom (manual inputs)"


# =====================================================
# GLASSMORPHISM CSS
# =====================================================
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%,
            rgba(42, 157, 143, 0.20), transparent 30%),
        radial-gradient(circle at 90% 15%,
            rgba(99, 102, 241, 0.20), transparent 28%),
        linear-gradient(135deg, #0b1220, #111827 55%, #172033);
    color: #f8fafc;
}

.block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3, p, label {
    color: #f8fafc !important;
}

.hero {
    padding: 2rem;
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(18px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.22);
    margin-bottom: 1.5rem;
}

.hero-tag {
    color: #5eead4;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    font-size: 2.5rem;
    margin: 0.5rem 0;
}

.hero p {
    color: #cbd5e1 !important;
    font-size: 1.05rem;
}

.glass-card {
    padding: 1.4rem;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.065);
    border: 1px solid rgba(255, 255, 255, 0.13);
    backdrop-filter: blur(16px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.16);
    margin-bottom: 1rem;
}

.section-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #f8fafc;
}

div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stCheckbox"] label {
    color: #e2e8f0 !important;
    font-weight: 600;
}

div[data-testid="stSelectbox"] > div > div {
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 12px;
}

div[data-testid="stCheckbox"] {
    padding: 0.65rem 0.8rem;
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    margin-bottom: 0.5rem;
}

div[data-testid="stCheckbox"] label {
    display: flex;
    align-items: center;
}

div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 3.2rem;
    border-radius: 14px;
    border: 1px solid rgba(94, 234, 212, 0.45);
    background: linear-gradient(90deg, #0f766e, #0d9488);
    color: white;
    font-size: 1.05rem;
    font-weight: 700;
    transition: 0.2s ease;
}

div[data-testid="stButton"] > button:hover {
    border-color: #99f6e4;
    background: linear-gradient(90deg, #115e59, #0f766e);
    transform: translateY(-2px);
}

.helper {
    color: #94a3b8;
    font-size: 0.85rem;
}

div[data-testid="stSlider"] [data-baseweb="slider"] {
    padding-top: 0.4rem;
}

footer {
    visibility: hidden;
}

@media (max-width: 700px) {
    .hero h1 {
        font-size: 1.8rem;
    }

    .hero {
        padding: 1.3rem;
    }
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO SECTION
# =====================================================
st.markdown("""
<div class="hero">
    <div class="hero-tag">
        Machine Learning • Demand Forecasting
    </div>
    <h1>🚲 Bike Demand AI</h1>
    <p>
        Explore how time and weather conditions may affect
        bike rental demand. Select a preset scenario or
        configure the conditions manually.
    </p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# PRESET SCENARIO SELECTOR
# =====================================================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🧪 Quick Test Scenarios</div>',
    unsafe_allow_html=True
)

st.selectbox(
    "Choose a preset scenario",
    options=list(SCENARIOS.keys()),
    key="scenario",
    on_change=apply_scenario
)

st.markdown(
    '<p class="helper">'
    'Choose a preset to automatically fill in the inputs below. '
    'You can also change the values manually.'
    '</p>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# TIME AND SCHEDULE
# =====================================================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📅 Time & Schedule</div>',
    unsafe_allow_html=True
)

time_col, season_col = st.columns(2)

with time_col:
    year = st.selectbox(
        "Training dataset year",
        options=[2011, 2012],
        key="year",
        help="The model was trained on historical data from 2011–2012."
    )

    hour = st.selectbox(
        "Time of day",
        options=list(range(24)),
        format_func=lambda h: (
            f"{h:02d}:00 — "
            f"{'Midnight' if h == 0 else
               'Noon' if h == 12 else
               str(h if h < 12 else h - 12) +
               (' AM' if h < 12 else ' PM')}"
        ),
        key="hour"
    )

with season_col:
    season = st.selectbox(
        "Season",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "🌱 Spring",
            2: "☀️ Summer",
            3: "🍂 Fall",
            4: "❄️ Winter"
        }[x],
        key="season"
    )

    st.markdown("**Day type**")

    holiday = st.checkbox(
        "Public holiday",
        key="holiday"
    )

    workingday = st.checkbox(
        "Working day",
        key="workingday"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# WEATHER CONDITIONS
# =====================================================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🌦️ Weather Conditions</div>',
    unsafe_allow_html=True
)

weather = st.selectbox(
    "Weather category",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "☀️ Clear / Partly cloudy",
        2: "☁️ Mist / Cloudy",
        3: "🌧️ Light rain / Snow",
        4: "⛈️ Heavy rain / Snow"
    }[x],
    key="weather"
)

weather_col1, weather_col2 = st.columns(2)

with weather_col1:
    temp = st.slider(
        "Temperature (°C)",
        min_value=-10.0,
        max_value=40.0,
        step=0.5,
        key="temp"
    )

    atemp = st.slider(
        "Feels-like temperature (°C)",
        min_value=-10.0,
        max_value=50.0,
        step=0.5,
        key="atemp"
    )

with weather_col2:
    humidity = st.slider(
        "Humidity (%)",
        min_value=0,
        max_value=100,
        key="humidity"
    )

    windspeed = st.slider(
        "Wind speed",
        min_value=0.0,
        max_value=60.0,
        step=0.5,
        key="windspeed"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# PREDICTION
# =====================================================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🔮 Get a Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="helper">'
    'Estimate hourly bike rental demand using your trained model.'
    '</p>',
    unsafe_allow_html=True
)

if st.button("Predict Bike Demand", type="primary"):

    # Build input row
    input_data = {
        "id": 0,
        "year": year,
        "hour": hour,
        "holiday": int(holiday),
        "workingday": int(workingday),
        "temp": temp,
        "atemp": atemp,
        "humidity": humidity,
        "windspeed": windspeed,

        # Cyclical time features
        "hour_sin": np.sin(2 * np.pi * hour / 24),
        "hour_cos": np.cos(2 * np.pi * hour / 24),
    }

    # One-hot encode season
    for s in range(1, 5):
        input_data[f"season_{s}"] = int(season == s)

    # One-hot encode weather
    for w in range(1, 4):
        input_data[f"weather_{w}"] = int(weather == w)

    # Create dataframe and align with training features
    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(
        columns=model_features,
        fill_value=0
    )

    # Generate prediction
    prediction = model.predict(input_df)[0]

    # Demand cannot be negative
    prediction = max(0, prediction)

    st.success("Prediction completed!")


    # Round prediction for displaying an estimated rental count
    predicted_count = max(0, int(round(prediction)))

    # Display predicted rental count
    st.metric(
        label="Estimated Bike Rentals",
        value=f"{predicted_count:,}",
        help="Estimated rental count for the selected hour."
    )

    # Interpret demand using dataset quartiles
    if predicted_count <= 41:
        demand_level = "Low"
        demand_message = (
            "Demand is in the lowest quarter of your training data."
        )
        demand_color = "#60a5fa"

    elif predicted_count <= 145:
        demand_level = "Moderate"
        demand_message = (
            "Demand is above the lowest quarter, "
            "but at or below the dataset median."
        )
        demand_color = "#facc15"

    elif predicted_count <= 283:
        demand_level = "High"
        demand_message = (
            "Demand is above the dataset median, "
            "but at or below the 75th percentile."
        )
        demand_color = "#fb923c"

    else:
        demand_level = "Very High"
        demand_message = (
            "Demand is above the 75th percentile "
            "of your training data."
        )
        demand_color = "#4ade80"

    # Display demand category
    st.markdown(
        f"""
        <div style="
            margin-top: 1rem;
            padding: 1rem 1.2rem;
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid {demand_color};
        ">
            <div style="
                color: {demand_color};
                font-size: 0.8rem;
                font-weight: 700;
                letter-spacing: 1.5px;
                text-transform: uppercase;
            ">
                Demand Level
            </div>
            <div style="
                color: #f8fafc;
                font-size: 1.6rem;
                font-weight: 700;
                margin: 0.3rem 0;
            ">
                {demand_level}
            </div>
            <div style="color: #cbd5e1;">
                {demand_message}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "This is an estimate from your trained model, "
        "not a live rental count. Categories are based "
        "on your training dataset's quartiles."
    )

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================
st.markdown(
    '<p class="helper" style="text-align:center; margin-top:2rem;">'
    'Bike Demand AI • Academic Machine Learning Project'
    '</p>',
    unsafe_allow_html=True
)