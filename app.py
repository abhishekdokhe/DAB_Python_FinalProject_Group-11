from flask import Flask, render_template
from pathlib import Path
import sqlite3

base_path = Path.cwd()
db_name = "ElectricCar.db"
file_path = base_path / 'database' / db_name
# print(file_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cars = cursor.execute("SELECT * FROM ElectricCar").fetchall()


    columnNames = cursor.execute("PRAGMA table_info(ElectricCar)").fetchall()
    columns = [column[1] for column in columnNames]
    conn.close()

    return render_template("data.html", cars = cars, columns = columns)

if __name__=="__main__":
    app.run(debug=True)