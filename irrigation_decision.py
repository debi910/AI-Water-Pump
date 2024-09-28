'''import requests
import json


class IrrigationSystem:
    def __init__(self, soil_moisture_sensor, weather_api_key, crop_type):
        self.soil_moisture_sensor = soil_moisture_sensor
        self.weather_api_key = weather_api_key
        self.crop_type = crop_type
        self.weather_data = None

    def get_soil_moisture(self):
        # Simulate reading from the soil moisture sensor
        return self.soil_moisture_sensor.read_moisture()

    def fetch_weather_data(self, location):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.weather_api_key}&q={location}"
        response = requests.get(url)
        self.weather_data = response.json()

    def should_irrigate(self):
        moisture = self.get_soil_moisture()
        rain_forecast = self.weather_data['current']['precip_mm'] > 0

        # Example threshold values
        moisture_threshold = 30  # Moisture level below which irrigation is needed

        if moisture < moisture_threshold and not rain_forecast:
            return True
        return False

    def irrigate(self):
        if self.should_irrigate():
            print("Irrigating the crop.")
            # Code to trigger irrigation system
        else:
            print("No irrigation needed.")


# Example usage
class SoilMoistureSensor:
    def read_moisture(self):
        # Simulate reading soil moisture level
        return 25  # Example moisture level


sensor = SoilMoistureSensor()
irrigation_system = IrrigationSystem(sensor, "YOUR_WEATHER_API_KEY", "Tomato")
irrigation_system.fetch_weather_data("YourLocation")
irrigation_system.irrigate()'''

'''import requests
import json
import numpy as np
from sklearn.linear_model import LinearRegression

# Constants for API endpoints (example URLs)
SOIL_MOISTURE_API = "http://api.soilmoisture.com"
WEATHER_API = "http://api.weather.com"
RAIN_FORECAST_API = "http://api.rainforecast.com"
CROP_DATA_API = "http://api.cropdata.com"


# Function to get data from APIs
def get_data():
    soil_moisture = requests.get(SOIL_MOISTURE_API).json()
    weather = requests.get(WEATHER_API).json()
    rain_forecast = requests.get(RAIN_FORECAST_API).json()
    crop_data = requests.get(CROP_DATA_API).json()

    return soil_moisture, weather, rain_forecast, crop_data


# Example function to decide irrigation needs
def irrigation_decision(soil_moisture, weather, rain_forecast, crop_type):
    moisture_level = soil_moisture['level']
    rainfall_pred = rain_forecast['predicted']

    # Simple logic to decide irrigation
    if moisture_level < 30 and rainfall_pred < 5:  # Example thresholds
        return "Irrigate"
    elif moisture_level >= 30:
        return "No need to irrigate"
    else:
        return "Check weather forecast"


# Main function
def main():
    soil_moisture, weather, rain_forecast, crop_data = get_data()
    crop_type = crop_data['type']

    decision = irrigation_decision(soil_moisture, weather, rain_forecast, crop_type)
    print(f"Irrigation decision for {crop_type}: {decision}")


if __name__ == "__main__":
    main()'''
'''
import requests
import json
import logging
from sklearn.linear_model import LinearRegression

# Configuration
API_ENDPOINTS = {
    'soil_moisture': 30,
    'weather': 'rain',
    'rain_forecast': 23,
    'crop_data': 'rice'
}
MOISTURE_THRESHOLD = 30
RAIN_THRESHOLD = 5

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching data from {api_url}: {e}")
        return None


def irrigation_decision(soil_moisture, rain_forecast):
    if soil_moisture < MOISTURE_THRESHOLD and rain_forecast < RAIN_THRESHOLD:
        return "Irrigate"
    return "No irrigation needed"


def main():
    soil_moisture_data = get_data(API_ENDPOINTS['soil_moisture'])
    weather_data = get_data(API_ENDPOINTS['weather'])
    rain_forecast_data = get_data(API_ENDPOINTS['rain_forecast'])
    crop_data = get_data(API_ENDPOINTS['crop_data'])

    if not all([soil_moisture_data, weather_data, rain_forecast_data, crop_data]):
        logging.error("Failed to retrieve all data. Exiting.")
        return

    soil_moisture = soil_moisture_data.get('moisture_level', 0)
    rain_forecast = rain_forecast_data.get('forecast', 0)

    decision = irrigation_decision(soil_moisture, rain_forecast)
    logging.info(f"Decision: {decision}")


if __name__ == "__main__":
    main()'''

'''from flask import Flask, render_template, request

app = Flask(__name__)


# The function that adjusts irrigation based on sensor inputs
def adjust_irrigation(soil_moisture, temperature, pH_level, turbidity, crop_data):
    flow_rate = 0
    pump_status = 0
    if crop_data['water_consumption_stage'] == 'high':
        if soil_moisture < 60:
            flow_rate = 15
            pump_status = 1
        else:
            pump_status = 0
    elif crop_data['water_consumption_stage'] == 'medium':
        if soil_moisture < 50:
            flow_rate = 10
            pump_status = 1
        else:
            pump_status = 0
    elif crop_data['water_consumption_stage'] == 'low':
        if soil_moisture < 40:
            flow_rate = 5
            pump_status = 1
        else:
            pump_status = 0
    return {"flow_rate": flow_rate, "pump_status": pump_status}


# Route for displaying form
@app.route('/')
def home():
    return render_template('form.html')


# Route for handling form submission
@app.route('/adjust_irrigation', methods=['POST'])
def irrigation():
    soil_moisture = float(request.form['soil_moisture'])
    temperature = float(request.form['temperature'])
    pH_level = float(request.form['pH_level'])
    turbidity = float(request.form['turbidity'])
    crop_name = request.form['crop_name']
    water_stage = request.form['water_stage']

    crop_data = {'name': crop_name, 'water_consumption_stage': water_stage}

    result = adjust_irrigation(soil_moisture, temperature, pH_level, turbidity, crop_data)
    return f"Flow Rate: {result['flow_rate']} L/min, Pump Status: {'ON' if result['pump_status'] == 1 else 'OFF'}"


if __name__ == '__main__':
    app.run(debug=True)'''

'''import requests
import json
import logging
from sklearn.linear_model import LinearRegression

# Configuration
API_ENDPOINTS = {
    'soil_moisture': 'https://api.example.com/soil_moisture',
    'weather': 'https://api.example.com/weather',
    'rain_forecast': 'https://api.example.com/rain_forecast',
    'crop_data': 'https://api.example.com/crop_data'
}
MOISTURE_THRESHOLD = 30
RAIN_THRESHOLD = 5

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching data from {api_url}: {e}")
        return None


def irrigation_decision(soil_moisture, rain_forecast):
    if soil_moisture < MOISTURE_THRESHOLD and rain_forecast < RAIN_THRESHOLD:
        return "Irrigate"
    return "No irrigation needed"


def main():
    soil_moisture_data = get_data(API_ENDPOINTS['soil_moisture'])
    weather_data = get_data(API_ENDPOINTS['weather'])
    rain_forecast_data = get_data(API_ENDPOINTS['rain_forecast'])
    crop_data = get_data(API_ENDPOINTS['crop_data'])

    if not all([soil_moisture_data, weather_data, rain_forecast_data, crop_data]):
        logging.error("Failed to retrieve all data. Exiting.")
        return

    soil_moisture = soil_moisture_data.get('moisture_level', 0)
    rain_forecast = rain_forecast_data.get('forecast', 0)

    decision = irrigation_decision(soil_moisture, rain_forecast)
    logging.info(f"Decision: {decision}")


if __name__ == "__main__":
    main()'''

'''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

# Step 1: Load the CSV dataset
data = pd.read_csv('irrigation_data.csv')

# Step 2: Inspect data
print(data.head())

# Step 3: Split data into features (X) and target (y)
X = data[['soil_moisture(%)', 'temperature', 'flowrate', 'ph_level', 'turbidity']]
y = data['pump_status']  # Assuming pump_status is binary: 0 = Off, 1 = On

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model using RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix: \n{conf_matrix}')
'''
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
data = pd.read_csv('irrigation_data.csv')
X = data[['soil_moisture', 'temperature', 'humidity', 'rain_forecast']]
y = data['pump_status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, 'smart_pump_model.pkl')
model = joblib.load('smart_pump_model.pkl')
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
real_time_data = pd.DataFrame([[30, 22, 60, 0]], columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])
pump_status = model.predict(real_time_data)
print('Pump Status:', 'ON' if pump_status[0] == 1 else 'OFF')import numpy as np'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
data = pd.read_csv('expanded_irrigation_data.csv')
X = data[['soil_moisture', 'temperature', 'humidity', 'rain_forecast']]
y = data['pump_status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, 'smart_pump_model.pkl')
model = joblib.load('smart_pump_model.pkl')
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
real_time_data = pd.DataFrame([[90, 50, 60, 0]], columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])
pump_status = model.predict(real_time_data)
print('Pump Status:', 'ON' if pump_status[0] == 1 else 'OFF')

