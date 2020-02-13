import os 
import datetime as dt
import numpy as  np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func, inspect
from flask import Flask,jsonify
from pprint import pprint

# database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect the  database into ORM class
# create automap
Base = automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)

# Create our session (link) from Python to the DB/start a session to query the databse
session = Session(engine)

# Use the inspector to Explore the database and print the table names
inspector = inspect(engine)
inspector.get_table_names()
# We can view all of the classes that automap found
Base.classes.keys()
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

#Flask Routes

@app.route("/")
def homepage():
    """List All Available Api Routes"""
    return(
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    """ Return a list of all prcp names"""
    """Return the JSON representation of your dictionary"""




    return
@app.route('/api/v1.0/stations')
def stations():
    """ Return a JSON list of stations from the dataset"""
    return

@app.route('/api/v1.0/tobs')
def tobs():
"""Return a JSON list of Temperature Observations (tobs) for the previous year"""
return
@app.route('/api/v1.0/<start>')
def temp_start()
""""Return a JSON list of The `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date. """
return

@app.route('/api/v1.0/<start>/<end>')
def temp_start_end()
"""""""Return a JSON list of The `TMIN`, `TAVG`, and `TMAX` for the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive."""
return