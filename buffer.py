'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('smart_pump_model.pkl')

def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)

        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')

root = tk.Tk()
root.title('Smart Pump Controller')

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50')
header_frame.pack(padx=10, pady=10)

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#f2f2f2')
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=0, column=0, padx=5, pady=5)
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#f2f2f2').grid(row=1, column=0, padx=5, pady=5)
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=2, column=0, padx=5, pady=5)
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (rain=1,no_rain=0)', font=('Arial', 14), bg='#f2f2f2').grid(row=3, column=0, padx=5, pady=5)
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2')
button_frame.pack(padx=10, pady=10)

predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14))
predict_button.pack(padx=10, pady=10)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2')
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack(padx=10, pady=10)

root.mainloop()'''


'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('smart_pump_model.pkl')

# Predict pump status function
def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')

# Clear all input fields
def clear_fields():
    soil_moisture_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)
    humidity_entry.delete(0, tk.END)
    rain_forecast_entry.delete(0, tk.END)
    result_label.config(text='Pump Status: ')

# Main application window
root = tk.Tk()
root.title('Smart Pump Controller')
root.geometry('400x400')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
input_frame.pack(padx=10, pady=10, fill='x')

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=0, column=0, padx=5, pady=5, sticky='e')
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#f2f2f2').grid(row=1, column=0, padx=5, pady=5, sticky='e')
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=2, column=0, padx=5, pady=5, sticky='e')
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (1=rain, 0=no rain)', font=('Arial', 14), bg='#f2f2f2').grid(row=3, column=0, padx=5, pady=5, sticky='e')
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Clear button
clear_button = tk.Button(button_frame, text='Clear', command=clear_fields,
                         bg='#FF5733', fg='white', font=('Arial', 14), width=20)
clear_button.grid(row=1, column=0, padx=5, pady=5)

# Exit button
exit_button = tk.Button(button_frame, text='Exit', command=root.quit,
                        bg='#C70039', fg='white', font=('Arial', 14), width=20)
exit_button.grid(row=2, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Footer
footer_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
footer_frame.pack(fill='x')

tk.Label(footer_frame, text='Created by Your Name', font=('Arial', 10), bg='#4CAF50', fg='white').pack()

root.mainloop()'''
'''
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('smart_pump_model.pkl')

# Predict pump status function
def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')

# Clear all input fields
def clear_fields():
    soil_moisture_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)
    humidity_entry.delete(0, tk.END)
    rain_forecast_entry.delete(0, tk.END)
    result_label.config(text='Pump Status: ')

# Main application window
root = tk.Tk()
root.title('Smart Pump Controller')
root.geometry('400x400')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
input_frame.pack(padx=10, pady=10, fill='x')

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=0, column=0, padx=5, pady=5, sticky='e')
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#f2f2f2').grid(row=1, column=0, padx=5, pady=5, sticky='e')
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=2, column=0, padx=5, pady=5, sticky='e')
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (1=rain, 0=no rain)', font=('Arial', 14), bg='#f2f2f2').grid(row=3, column=0, padx=5, pady=5, sticky='e')
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Clear button
clear_button = tk.Button(button_frame, text='Clear', command=clear_fields,
                         bg='#FF5733', fg='white', font=('Arial', 14), width=20)
clear_button.grid(row=1, column=0, padx=5, pady=5)

# Exit button
exit_button = tk.Button(button_frame, text='Exit', command=root.quit,
                        bg='#C70039', fg='white', font=('Arial', 14), width=20)
exit_button.grid(row=2, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Footer
footer_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
footer_frame.pack(fill='x')

tk.Label(footer_frame, text='Created by Your Name', font=('Arial', 10), bg='#4CAF50', fg='white').pack()

root.mainloop()
'''
'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('smart_pump_model.pkl')

# Mock sensor data
current_data = {
    'soil_moisture': random.uniform(30, 70),
    'temperature': random.uniform(20, 35),
    'humidity': random.uniform(40, 80),
    'rain_forecast': random.choice([0, 1])
}


# Function to update current sensor data (simulated)
def update_sensor_data():
    current_data['soil_moisture'] = random.uniform(30, 70)
    current_data['temperature'] = random.uniform(20, 35)
    current_data['humidity'] = random.uniform(40, 80)
    current_data['rain_forecast'] = random.choice([0, 1])

    display_current_data()


def display_current_data():
    # Update labels with current sensor data
    soil_moisture_label.config(text=f"Soil Moisture: {current_data['soil_moisture']:.2f}%")
    temperature_label.config(text=f"Temperature: {current_data['temperature']:.2f}°C")
    humidity_label.config(text=f"Humidity: {current_data['humidity']:.2f}%")
    rain_label.config(text=f"Rain Forecast: {'Rain' if current_data['rain_forecast'] == 1 else 'No Rain'}")

    # Update the graph
    update_graph()


def predict_pump_status():
    try:
        real_time_data = pd.DataFrame([[current_data['soil_moisture'], current_data['temperature'],
                                        current_data['humidity'], current_data['rain_forecast']]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
    except ValueError:
        messagebox.showerror('Error', 'Error in processing data.')


# Function to plot graphs
def update_graph():
    # Generate some data for demonstration
    times = list(range(10))  # Dummy timestamps
    soil_moisture_values = [random.uniform(30, 70) for _ in range(10)]
    temperature_values = [random.uniform(20, 35) for _ in range(10)]

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(times, soil_moisture_values, label="Soil Moisture (%)", marker='o')
    ax.plot(times, temperature_values, label="Temperature (°C)", marker='o', linestyle='--')

    ax.set_title("Sensor Data over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()

    # Display the graph in Tkinter
    for widget in graph_frame.winfo_children():
        widget.destroy()  # Clear previous graph

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Main application window
root = tk.Tk()
root.title('Smart Pump Controller with Sensor Data')
root.geometry('600x600')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create sensor data frame
sensor_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
sensor_frame.pack(padx=10, pady=10)

tk.Label(sensor_frame, text='Current Sensor Data:', font=('Arial', 18), bg='#f2f2f2').grid(row=0, column=0,
                                                                                           columnspan=2, padx=5,
                                                                                           pady=10)

soil_moisture_label = tk.Label(sensor_frame, text=f"Soil Moisture: {current_data['soil_moisture']:.2f}%",
                               font=('Arial', 14), bg='#f2f2f2')
soil_moisture_label.grid(row=1, column=0, padx=5, pady=5)

temperature_label = tk.Label(sensor_frame, text=f"Temperature: {current_data['temperature']:.2f}°C", font=('Arial', 14),
                             bg='#f2f2f2')
temperature_label.grid(row=2, column=0, padx=5, pady=5)

humidity_label = tk.Label(sensor_frame, text=f"Humidity: {current_data['humidity']:.2f}%", font=('Arial', 14),
                          bg='#f2f2f2')
humidity_label.grid(row=3, column=0, padx=5, pady=5)

rain_label = tk.Label(sensor_frame,
                      text=f"Rain Forecast: {'Rain' if current_data['rain_forecast'] == 1 else 'No Rain'}",
                      font=('Arial', 14), bg='#f2f2f2')
rain_label.grid(row=4, column=0, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Update sensor button
update_button = tk.Button(button_frame, text='Update Sensor Data', command=update_sensor_data,
                          bg='#2196F3', fg='white', font=('Arial', 14), width=20)
update_button.grid(row=1, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Graph Frame
graph_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
graph_frame.pack(padx=10, pady=10)

# Display initial sensor data and graph
display_current_data()

# Footer
footer_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
footer_frame.pack(fill='x')

tk.Label(footer_frame, text='Created by Your Name', font=('Arial', 10), bg='#4CAF50', fg='white').pack()

root.mainloop()'''

'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('smart_pump_model.pkl')

# Predict pump status function
def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
        blink_result_label()  # Trigger animation effect
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')

# Clear all input fields
def clear_fields():
    soil_moisture_entry.delete(0, tk.END)
    temperature_entry.delete(0, tk.END)
    humidity_entry.delete(0, tk.END)
    rain_forecast_entry.delete(0, tk.END)
    result_label.config(text='Pump Status: ', fg='black')  # Reset color

# Function to simulate blinking of the result label
def blink_result_label():
    current_color = result_label.cget("fg")
    next_color = 'green' if current_color == 'black' else 'black'
    result_label.config(fg=next_color)
    result_label.after(500, blink_result_label)  # Repeat every 500 ms

# Main application window
root = tk.Tk()
root.title('Smart Pump Controller')
root.geometry('500x500')  # Set the size of the window

# Set professional background color
root.configure(bg='#2C3E50')

# Add an image to the application (ensure the file path is correct)
image_frame = tk.Frame(root, bg='#2C3E50')
image_frame.pack(pady=10)
pump_img = tk.PhotoImage(file="pump_image.png")  # Replace with your image file path
img_label = tk.Label(image_frame, image=pump_img, bg='#2C3E50')
img_label.pack()

# Create header frame
header_frame = tk.Frame(root, bg='#1ABC9C', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#1ABC9C', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#ECF0F1', padx=10, pady=10)
input_frame.pack(padx=10, pady=10, fill='x')

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#ECF0F1').grid(row=0, column=0, padx=5, pady=5, sticky='e')
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#ECF0F1').grid(row=1, column=0, padx=5, pady=5, sticky='e')
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#ECF0F1').grid(row=2, column=0, padx=5, pady=5, sticky='e')
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (1=rain, 0=no rain)', font=('Arial', 14), bg='#ECF0F1').grid(row=3, column=0, padx=5, pady=5, sticky='e')
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#ECF0F1', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#27AE60', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Clear button
clear_button = tk.Button(button_frame, text='Clear', command=clear_fields,
                         bg='#E74C3C', fg='white', font=('Arial', 14), width=20)
clear_button.grid(row=1, column=0, padx=5, pady=5)

# Exit button
exit_button = tk.Button(button_frame, text='Exit', command=root.quit,
                        bg='#C0392B', fg='white', font=('Arial', 14), width=20)
exit_button.grid(row=2, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#ECF0F1', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#ECF0F1')
result_label.pack()

# Footer
footer_frame = tk.Frame(root, bg='#1ABC9C', padx=10, pady=10)
footer_frame.pack(fill='x')

tk.Label(footer_frame, text='Created by Your Name', font=('Arial', 10), bg='#1ABC9C', fg='white').pack()

root.mainloop()'''

'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the trained model
try:
    model = joblib.load('smart_pump_model.pkl')
except FileNotFoundError:
    messagebox.showerror('Error', 'Model file not found. Ensure smart_pump_model.pkl is in the correct directory.')

# Mock sensor data
current_data = {
    'soil_moisture': random.uniform(30, 70),
    'temperature': random.uniform(20, 35),
    'humidity': random.uniform(40, 80),
    'rain_forecast': random.choice([0, 1])
}


# Function to update current sensor data (simulated)
def update_sensor_data():
    current_data['soil_moisture'] = random.uniform(30, 70)
    current_data['temperature'] = random.uniform(20, 35)
    current_data['humidity'] = random.uniform(40, 80)
    current_data['rain_forecast'] = random.choice([0, 1])

    display_current_data()


def display_current_data():
    # Update labels with current sensor data
    soil_moisture_label.config(text=f"Soil Moisture: {current_data['soil_moisture']:.2f}%")
    temperature_label.config(text=f"Temperature: {current_data['temperature']:.2f}°C")
    humidity_label.config(text=f"Humidity: {current_data['humidity']:.2f}%")
    rain_label.config(text=f"Rain Forecast: {'Rain' if current_data['rain_forecast'] == 1 else 'No Rain'}")

    # Update the graph
    update_graph()


def predict_pump_status():
    try:
        real_time_data = pd.DataFrame([[current_data['soil_moisture'], current_data['temperature'],
                                        current_data['humidity'], current_data['rain_forecast']]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])
        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
    except ValueError:
        messagebox.showerror('Error', 'Error in processing data.')


# Function to plot graphs
def update_graph():
    # Generate some data for demonstration
    times = list(range(10))  # Dummy timestamps
    soil_moisture_values = [random.uniform(30, 70) for _ in range(10)]
    temperature_values = [random.uniform(20, 35) for _ in range(10)]

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(times, soil_moisture_values, label="Soil Moisture (%)", marker='o')
    ax.plot(times, temperature_values, label="Temperature (°C)", marker='o', linestyle='--')
    ax.set_title("Sensor Data over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()

    # Display the graph in Tkinter
    for widget in graph_frame.winfo_children():
        widget.destroy()  # Clear previous graph
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Main application window
root = tk.Tk()
root.title('Smart Pump Controller with Sensor Data')
root.geometry('600x600')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width
tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create sensor data frame
sensor_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
sensor_frame.pack(padx=10, pady=10)
tk.Label(sensor_frame, text='Current Sensor Data:', font=('Arial', 18), bg='#f2f2f2').grid(row=0, column=0,
                                                                                           columnspan=2, padx=5,
                                                                                           pady=10)
soil_moisture_label = tk.Label(sensor_frame, text=f"Soil Moisture: {current_data['soil_moisture']:.2f}%",
                               font=('Arial', 14), bg='#f2f2f2')
soil_moisture_label.grid(row=1, column=0, padx=5, pady=5)
temperature_label = tk.Label(sensor_frame, text=f"Temperature: {current_data['temperature']:.2f}°C", font=('Arial', 14),
                             bg='#f2f2f2')
temperature_label.grid(row=2, column=0, padx=5, pady=5)
humidity_label = tk.Label(sensor_frame, text=f"Humidity: {current_data['humidity']:.2f}%", font=('Arial', 14),
                          bg='#f2f2f2')
humidity_label.grid(row=3, column=0, padx=5, pady=5)
rain_label = tk.Label(sensor_frame,
                      text=f"Rain Forecast: {'Rain' if current_data['rain_forecast'] == 1 else 'No Rain'}",
                      font=('Arial', 14), bg='#f2f2f2')
rain_label.grid(row=4, column=0, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Update sensor button
update_button = tk.Button(button_frame, text='Update Sensor Data', command=update_sensor_data,
                          bg='#2196F3', fg='white', font=('Arial', 14), width=20)
update_button.grid(row=1, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)
result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Graph Frame
graph_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
graph_frame.pack(padx=10, pady=10)

# Display initial sensor data and graph
display_current_data()

# Footer
footer_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
footer_frame.pack(fill='x')
tk.Label(footer_frame, text='Created by Your Name', font=('Arial', 10), bg='#4CAF50', fg='white').pack()

root.mainloop()'''

'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
# Load the trained model
model = joblib.load('smart_pump_model.pkl')

# Set the irrigation cycle time (in seconds)
irrigation_cycle_time = 60  # Example: 60 seconds
remaining_time = irrigation_cycle_time  # Remaining time for the countdown


# Function to predict pump status based on user inputs
def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)

        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')


# Function to plot graphs
def update_graph():
    # Generate some data for demonstration
    times = list(range(10))  # Dummy timestamps
    soil_moisture_values = [random.uniform(30, 70) for _ in range(10)]
    temperature_values = [random.uniform(20, 35) for _ in range(10)]

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(times, soil_moisture_values, label="Soil Moisture (%)", marker='o')
    ax.plot(times, temperature_values, label="Temperature (°C)", marker='o', linestyle='--')

    ax.set_title("Sensor Data over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    ax.legend()

    # Display the graph in Tkinter
    for widget in graph_frame.winfo_children():
        widget.destroy()  # Clear previous graph

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Function to update the countdown timer
def update_timer():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        minutes, seconds = divmod(remaining_time, 60)
        timer_label.config(text=f"Time Left for Next Irrigation: {minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)  # Call this function again after 1 second
    else:
        timer_label.config(text="Irrigation cycle started!")  # When countdown reaches zero


# Main application window
root = tk.Tk()
root.title('Smart Pump Controller with Timer')
root.geometry('600x600')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=0, column=0, padx=5, pady=5)
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#f2f2f2').grid(row=1, column=0, padx=5, pady=5)
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=2, column=0, padx=5, pady=5)
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (1=Rain, 0=No Rain)', font=('Arial', 14), bg='#f2f2f2').grid(row=3, column=0,
                                                                                                       padx=5, pady=5)
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Graph Frame
graph_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
graph_frame.pack(padx=10, pady=10)

# Display initial graph
update_graph()

# Timer frame
timer_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
timer_frame.pack(padx=10, pady=10)

timer_label = tk.Label(timer_frame, text='Time Left for Next Irrigation: 01:00', font=('Arial', 18), bg='#f2f2f2')
timer_label.pack()

# Footer
footer_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
footer_frame.pack(fill='x')

tk.Label(footer_frame, text='Created by Your Name', font=('Arial', 10), bg='#4CAF50', fg='white').pack()

# Start the countdown timer
root.after(1000, update_timer)

root.mainloop()
'''

'''import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('smart_pump_model.pkl')


# Function to calculate irrigation timer based on soil moisture
def calculate_irrigation_time(soil_moisture):
    if soil_moisture > 60:
        return 120  # 120 minutes for high moisture
    elif soil_moisture > 40:
        return 60  # 60 minutes for moderate moisture
    else:
        return 30  # 30 minutes for low moisture


# Function to update the irrigation timer
def update_timer():
    global timer_running
    if timer_running:
        if timer_seconds > 0:
            timer_seconds -= 1
            timer_label.config(text=f"Time until next irrigation: {timer_seconds} seconds")
            root.after(1000, update_timer)  # Update timer every second
        else:
            timer_label.config(text="Irrigation cycle complete!")
            timer_running = False


# Function to predict pump status and set the timer
def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')

        # Calculate and set timer based on soil moisture
        global timer_seconds, timer_running
        timer_seconds = calculate_irrigation_time(soil_moisture)
        timer_running = True
        update_timer()

    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')


# Initialize timer variables
timer_seconds = 0
timer_running = False

# Main application window
root = tk.Tk()
root.title('Smart Pump Controller with Timer')
root.geometry('600x600')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=0, column=0, padx=5, pady=5)
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#f2f2f2').grid(row=1, column=0, padx=5, pady=5)
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=2, column=0, padx=5, pady=5)
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (rain=1,no_rain=0)', font=('Arial', 14), bg='#f2f2f2').grid(row=3, column=0,
                                                                                                      padx=5, pady=5)
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Timer label
timer_label = tk.Label(root, text="Time until next irrigation: 0 seconds", font=('Arial', 14), bg='#f2f2f2')
timer_label.pack(pady=10)

root.mainloop()'''

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('smart_pump_model.pkl')

# Mock sensor data history for graphing
sensor_data_history = {
    'soil_moisture': [],
    'temperature': [],
    'humidity': [],
    'rain_forecast': []
}


# Function to update the graph
def update_graph():
    fig, ax = plt.subplots(figsize=(6, 4))  # Make the graph larger
    ax.plot(sensor_data_history['soil_moisture'], label="Soil Moisture (%)", marker='o')
    ax.plot(sensor_data_history['temperature'], label="Temperature (°C)", marker='o', linestyle='--')
    ax.plot(sensor_data_history['humidity'], label="Humidity (%)", marker='o', linestyle='-.')

    ax.set_title("Sensor Data over Time")
    ax.set_xlabel("Time (arbitrary units)")
    ax.set_ylabel("Value")
    ax.legend()

    # Display the graph in Tkinter
    for widget in graph_frame.winfo_children():
        widget.destroy()  # Clear previous graph

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Function to predict pump status
def predict_pump_status():
    try:
        soil_moisture = float(soil_moisture_entry.get())
        temperature = float(temperature_entry.get())
        humidity = float(humidity_entry.get())
        rain_forecast = float(rain_forecast_entry.get())

        real_time_data = pd.DataFrame([[soil_moisture, temperature, humidity, rain_forecast]],
                                      columns=['soil_moisture', 'temperature', 'humidity', 'rain_forecast'])

        pump_status = model.predict(real_time_data)
        result = 'ON' if pump_status[0] == 1 else 'OFF'
        result_label.config(text=f'Pump Status: {result}')

        # Update sensor data history for graphing
        sensor_data_history['soil_moisture'].append(soil_moisture)
        sensor_data_history['temperature'].append(temperature)
        sensor_data_history['humidity'].append(humidity)
        sensor_data_history['rain_forecast'].append(rain_forecast)

        # Update graph with new data
        update_graph()

    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers')


# Main application window
root = tk.Tk()
root.title('Smart Pump Controller with Graph')
root.geometry('600x700')  # Set the size of the window

# Set background color
root.configure(bg='#f2f2f2')

# Create header frame
header_frame = tk.Frame(root, bg='#4CAF50', padx=10, pady=10)
header_frame.pack(fill='x')  # Expand the header to full width

tk.Label(header_frame, text='Smart Pump Controller', font=('Arial', 24), bg='#4CAF50', fg='white').pack()

# Create input frame
input_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text='Soil Moisture (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=0, column=0, padx=5, pady=5)
soil_moisture_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
soil_moisture_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Temperature (°C)', font=('Arial', 14), bg='#f2f2f2').grid(row=1, column=0, padx=5, pady=5)
temperature_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
temperature_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Humidity (%)', font=('Arial', 14), bg='#f2f2f2').grid(row=2, column=0, padx=5, pady=5)
humidity_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
humidity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text='Rain Forecast (rain=1,no_rain=0)', font=('Arial', 14), bg='#f2f2f2').grid(row=3, column=0,
                                                                                                      padx=5, pady=5)
rain_forecast_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
rain_forecast_entry.grid(row=3, column=1, padx=5, pady=5)

# Create button frame
button_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
button_frame.pack(padx=10, pady=10)

predict_button = tk.Button(button_frame, text='Predict Pump Status', command=predict_pump_status,
                           bg='#4CAF50', fg='white', font=('Arial', 14), width=20)
predict_button.grid(row=0, column=0, padx=5, pady=5)

# Create result frame
result_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
result_frame.pack(padx=10, pady=10)

result_label = tk.Label(result_frame, text='Pump Status: ', font=('Arial', 18), bg='#f2f2f2')
result_label.pack()

# Graph Frame
graph_frame = tk.Frame(root, bg='#f2f2f2', padx=10, pady=10)
graph_frame.pack(padx=10, pady=10)

root.mainloop()
