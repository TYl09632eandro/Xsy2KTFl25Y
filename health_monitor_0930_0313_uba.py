# 代码生成时间: 2025-09-30 03:13:29
import numpy as np

"""
Health Monitor Application

This application simulates a health monitoring device using Python and NumPy.
It generates random health data, such as heart rate, blood pressure, and blood glucose levels,
and checks if the values are within the normal range.
"""

# Constants for healthy ranges
HEART_RATE_RANGE = (60, 100)  # BPM
BLOOD_PRESSURE_RANGE = (90, 120, 60, 80)  # Systolic, diastolic
BLOOD_GLUCOSE_RANGE = (70, 140)  # mg/dL

def generate_random_health_data():
    """Generates random health data for demonstration purposes."""
    heart_rate = np.random.randint(*HEART_RATE_RANGE)
    blood_pressure = np.random.randint(*BLOOD_PRESSURE_RANGE)
    blood_glucose = np.random.randint(*BLOOD_GLUCOSE_RANGE)
    return heart_rate, blood_pressure, blood_glucose

def check_health_data(heart_rate, blood_pressure, blood_glucose):
    """Checks if the provided health data is within the normal range."""
    try:
        if not (HEART_RATE_RANGE[0] <= heart_rate <= HEART_RATE_RANGE[1]):
            raise ValueError(f"Heart rate {heart_rate} is not within the normal range of {HEART_RATE_RANGE[0]}-{HEART_RATE_RANGE[1]} BPM.")
        if not (BLOOD_PRESSURE_RANGE[0] <= blood_pressure[0] <= BLOOD_PRESSURE_RANGE[1] and
                BLOOD_PRESSURE_RANGE[2] <= blood_pressure[1] <= BLOOD_PRESSURE_RANGE[3]):
            raise ValueError(
                f"Blood pressure {blood_pressure} is not within the normal range of {BLOOD_PRESSURE_RANGE[0]}-{BLOOD_PRESSURE_RANGE[1]}/{BLOOD_PRESSURE_RANGE[2]}-{BLOOD_PRESSURE_RANGE[3]}."
            )
        if not (BLOOD_GLUCOSE_RANGE[0] <= blood_glucose <= BLOOD_GLUCOSE_RANGE[1]):
            raise ValueError(f"Blood glucose {blood_glucose} is not within the normal range of {BLOOD_GLUCOSE_RANGE[0]}-{BLOOD_GLUCOSE_RANGE[1]} mg/dL.")
        return True
    except ValueError as e:
        print(e)
        return False

def main():
    """Main function to simulate health monitoring."""
    heart_rate, blood_pressure, blood_glucose = generate_random_health_data()
    print(f"Generated Health Data: Heart Rate = {heart_rate} BPM, Blood Pressure = {blood_pressure}, Blood Glucose = {blood_glucose} mg/dL")
    if check_health_data(heart_rate, blood_pressure, blood_glucose):
        print("All health data is within normal range.")
    else:
        print("Warning: Some health data is outside the normal range.")

def run():
    """Entry point for the application."""
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")

def __name__ == "__main__":
    run()
