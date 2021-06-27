# StarDust -> Phase 4 AstroPI ![AstroPI + ESA](https://github.com/DavidGhergut/StarDust_AstroPI/blob/master/Esa_AstroPI.jpg "Sugestive Image")

## Purpose of the program written

#### The python code inside the ```main.py``` file helped us make several calculations that made the process of making the report easier.

## Method of obtaining the desired data

#### In order to generate the wanted output, we edited the csv given in Phase 3 (```imported_data.csv```) by deleting all the columns except those of most interest: temperature, humidity, pressure and CPU temperature.

### *Then, we focused on three main results:*
#### 1️⃣ A new csv file that contains the temperature uninfluenced by the CPU (```resulted_data.csv```)
#### 📝 In order to get a closer temperature to the one on the ISS (from the Humidity and the Pressure sensors) we applied two formulas that we found out on the [AstroPI forum](https://www.raspberrypi.org/forums/viewtopic.php?t=111457):
* ```0.0071 * (temp_from_humidity ** 2) + 0.86 * temp_from_humidity - 10.0```
* ```temp_from_pressure - ((CPU_temp - temp_from_pressure) / 1.5)```
#### 2️⃣ Printing the average value for each data type / column
#### 3️⃣ Printing the min-max interval for each column, so that we how many and which plants will be able to live under these conditions

![Image about what we printed](https://github.com/DavidGhergut/StarDust_AstroPI/blob/master/Printed_data.png "Sugestive Image")

## ❗️This program does not use other modules than *csv* and *pathlib* ❗️
## ⚠️ All lines of code are written exclusively by the members of StarDust team for the Phase 4 of the AstroPI contest ⚠️
