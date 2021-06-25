"""
This code was written by team StarDust from Bucharest, Romania for Phase 4 AstroPI
Team members: 
David Ghergut
Andreea Patarlageanu
Ariadna Alexandrescu
Denisa Arsene
Ana Dobrescu
Andrei Stan
"""

from csv import *
from pathlib import Path

def csv_file_reader():
    nr = 1
    dir_path = Path(__file__).parent.resolve()
    manipulated_file = dir_path/'data.csv'
    avg_temperature_from_Humidity, avg_temperature_from_Pressure, avg_CPU_Temperature, avg_Humidity, avg_Pressure = 0.0, 0.0, 0.0, 0.0, 0.0
    max_temperature_from_Humidity, max_temperature_from_Pressure, max_CPU_Temperature, max_Humidity, max_Pressure = 0.0, 0.0, 0.0, 0.0, 0.0
    min_temperature_from_Humidity, min_temperature_from_Pressure, min_CPU_Temperature, min_Humidity, min_Pressure = 50.0, 50.0, 50.0, 50.0, 10000.0
    with open(str(manipulated_file), 'r') as data_file:
        csv_reader = reader(data_file, quoting=QUOTE_NONNUMERIC)
        for line in csv_reader:
            print(str(nr) + '.')
            #TEMPERATURE FROM THE HUMIDITY SENSOR
            CalcTemp1 = round((0.0071* (line[0] ** 2) + 0.86 * line[0] - 10.0), 2)
            print("temp_humidity: " + str(CalcTemp1))
            #TEMPERATURE FROM THE PRESSURE SENSOR
            #cpuTemp = float(line[2])
            #ambient = float(line[1])
            CalcTemp2 = round(line[1] - ((line[2] - line[1]) / 1.5), 2)
            print("temp_pressure: " + str(CalcTemp2))
            print('\n')
            #THE AVERAGE VALUE FOR ALMOST EACH TYPE OF DATA THAT WE COLLECTED
            avg_temperature_from_Humidity += line[0]
            avg_temperature_from_Pressure += line[1]
            avg_CPU_Temperature += line[2]
            avg_Humidity += line[3]
            avg_Pressure += line[4]
            #THE MINIMUM AND THE MAXIMUM VALUE FOR ALMOST EACH TYPE OF DATA THAT WE COLLECTED
            if line[0] < min_temperature_from_Humidity:
                min_temperature_from_Humidity = line[0]
            elif line[0] > max_temperature_from_Humidity:
                max_temperature_from_Humidity = line[0]
            if line[1] < min_temperature_from_Pressure:
                min_temperature_from_Pressure = line[1]
            elif line[1] > max_temperature_from_Pressure:
                max_temperature_from_Pressure = line[1]
            if line[2] < min_CPU_Temperature:
                min_CPU_Temperature = line[2]
            elif line[2] > max_CPU_Temperature:
                max_CPU_Temperature = line[2]
            if line[3] < min_Humidity:
                min_Humidity = line[3]
            elif line[3] > max_Humidity:
                max_Humidity = line[3]
            if line[4] < min_Pressure:
                min_Pressure = line[4]
            elif line[4] > max_Pressure:
                max_Pressure = line[4]
            nr += 1

                
    print("The average temperature from the Humidity sensor is: " + str(round(float(avg_temperature_from_Humidity / 417), 2)))
    print("The average temperature from the Pressure sensor is: " + str(round(float(avg_temperature_from_Pressure / 417), 2)))
    print("The average CPU Temperature is: " + str(round(float(avg_CPU_Temperature / 417), 2)))
    print("The average Humidity from the Humidity sensor is: " + str(round(float(avg_Humidity / 417), 2)))
    print("The average Pressure from the Pressure sensor is: " + str(round(float(avg_Pressure / 417), 2)))
    print('\n')
    print("The interval for temperature from the Humidity sensor is: " + str(min_temperature_from_Humidity) + "  ----->  " + str(max_temperature_from_Humidity))
    print("The interval for temperature from the Pressure sensor is: " + str(min_temperature_from_Pressure) + "  ----->  " + str(max_temperature_from_Pressure))
    print("The interval for CPU temperature is: " + str(min_CPU_Temperature) + "  ----->  " + str(max_CPU_Temperature))
    print("The interval for Humidity from the Humidity sensor is: " + str(min_Humidity) + "  ----->  " + str(max_Humidity))
    print("The interval for Pressure from the Pressure sensor is: " + str(min_Pressure) + "  ----->  " + str(max_Pressure))

csv_file_reader()