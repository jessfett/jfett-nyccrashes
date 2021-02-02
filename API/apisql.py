
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import requests
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
import os

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app, support_credentials=True)


DB_HOST = "localhost"
DB_NAME = "crashes_db"
DB_USER = "postgres"
DB_PASS = "S2up45p2!"

engine = create_engine('postgresql://postgres:S2up45p2!@localhost/crashes_db')



# DATABASE_URL = os.environ["DATABASE_URL"]
#engine = create_engine(DB_URL)

#Reflect database into ORM class
Base=automap_base()
Base.prepare(engine, reflect=True)
Info =Base.classes.crashes_2020


# Use the Inspector to explore the database and print the table names
inspector = inspect(engine)
inspector.get_table_names()


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/></br>"
        f"Crash Counts By Borough: /crashcount</br>"
        f"All Crashes Info: /crashinfo</br>"
        f"Injury Summary: /injuries</br>"
        
    )

@app.route("/crashcount")
def crashcount():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = engine.execute('SELECT * FROM "crash_count";')

    borough = []
    crash_count = []

    for result in results:
        city_borough = result.borough
        borough.append(city_borough)

        count = result.crashcount
        crash_count.append(count)


    session.close()

    return jsonify({'borough': borough, 'crashcounts': crash_count})



@app.route("/crashinfo")
def crashinfo():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    crashinforesults = engine.execute('SELECT * FROM "crashes_2020" LIMIT 10;')




    crashdate = []
    borough_info = []
    latitude = []
    longitude = []
    contributing_factor =[]
    crashid = []
    vehicle_type =[]

    for crash in crashinforesults:
        date = crash.crashdate
        crashdate.append(date)

        boroughname = crash.borough
        borough_info.append(boroughname)

        lat=crash.latitude    
        latitude.append(float(lat))

        lng = crash.longitude
        longitude.append(float(lng))

        factor = crash.contributingfactor
        contributing_factor.append(factor)

        crash_id = crash.collisionid
        crashid.append(crash_id)

        crash_vehicle = crash.vehicletype
        vehicle_type.append(crash_vehicle)

    session.close()

    return jsonify({'crash date': crashdate, 'borough': borough_info, 'latitude': latitude, 'longitude': longitude, 'Contributing Factor': contributing_factor, 'Collision ID': crashid, 'Vehicle Type': vehicle_type})

@app.route("/injuries")
def injuries():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    crashimpacts = engine.execute('SELECT * FROM "crash_impact" LIMIT 10;')

    impactborough = []
    persons_injured = []
    persons_killed = []
    pedestrians_injured = []
    pedestrians_killed =[]
    cyclist_injured = []
    cyclist_killed =[]
    motorist_injured =[]
    motorist_killed = []

    for impact in crashimpacts:
        Borough = impact.borough
        impactborough.append(Borough)

        per_injured = impact.peronsinjured
        persons_injured.append(float(per_injured))

        per_killed=impact.personskilled    
        persons_killed.append(float(per_killed))

        ped_injured = impact.pedestriansinjured
        pedestrians_injured.append(float(ped_injured))

        ped_killed = impact.pedestrianskilled
        pedestrians_killed.append(float(ped_killed))

        cyc_injured = impact.cyclistinjured
        cyclist_injured.append(float(cyc_injured))

        cyc_killed = impact.cyclistkilled
        cyclist_killed.append(float(cyc_killed))

        mot_injured = impact.motoristinjured
        motorist_injured.append(float(mot_injured))

        mot_killed = impact.motoristkilled
        motorist_killed.append(float(mot_killed))

    session.close()

    return jsonify({'borough': impactborough, 'Persons Injured': persons_injured, 'Persons Killed': persons_killed, 'Pedestrians Injured': pedestrians_injured, 'Pedestrians Killed': pedestrians_killed, 'Cyclist Injured': cyclist_injured, 'Cyclist Killed': cyclist_killed, 'Motorist Injured': motorist_injured, 'Motorist Killed': motorist_killed})



if __name__ == '__main__':
    app.run(debug=True)
