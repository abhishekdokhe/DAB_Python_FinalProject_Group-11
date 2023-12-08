# Python Final Project

### Group Members:

Group No. 11

 - Abhisek dokhe
 - Tanya Patel
 - Opeyemi Lateef
 
### Objective:

 - This project contains the usage of Python, Pandas, SQLite3, and Flask.
 - Flask is used to present stored data of database on web.
 - Website contains mainly 3 pages, Home, About Us, and Cars. 
 - About Us page shows the details about dataset and defination of each variable. 
 - Cars page shows the data stored in database using SQLite3.


## How to Run

 - Run command "pip install -r requirements.txt" to download required packages

 ### Run Website:

Step 1:
- Clone the project first or download zip of project and extract it

Step 2:
 - If you not see 'ElectricCar.db' file in database folder, then open new terminal in 'database' folder and run "python buildDB.py" command

Step 3:
 - Open 'terminal' or 'cmd' in root directory
 - Run "python app.py" command
 - Go to http://127.0.0.1:5000

## Electric Car Dataset

### Overview

This is a dataset of electric vehicles. One of the more popular data science datasets is the mtcars dataset. It is known for its simplicity when running analysis and visualizations. When looking for simple datasets on EVs, there don't seem to be any. Also, given the growth in this market, this is something many would be curious about. Hence, the reason for creating this dataset.

### Source of Data

*Link to Source:* [Dataset](https://www.kaggle.com/datasets/geoffnel/evs-one-electric-vehicle-dataset)

### Defination of Variables

 - Brand: Car Brands
 - Model: Model of the car
 - AccelSec: Cars acceleration
 - TopSpeed: Cars Top speed
 - Range_Km: Range of the car in kilometers
 - Efficiency_WhKm: KM range per Watt Hour
 - FastCharge_KmH: Charge speed per hour in KMs
 - RapidCharge: Rapid charge capability of the car
 - PowerTrain: Drive train platform of the car
 - PlugType: Charging plug type
 - BodyStyle: Body type of the car
 - Segment: Car Segment
 - Seats: Passenger capacity
 - PriceEuro: Price of the car in euros