import os
import datetime as dt
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
from pprint import pprint

# database Setup
engine = create_engine(
    "sqlite:///Resources/hawaii.sqlite", connect_args={"check_same_thread": False}
)
# reflect the  database into ORM class
# create automap
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

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
app = Flask(__name__) # the name of the file & the object(double usage)

# Flask Routes


@app.route("/")
def home():
    """List All Available Api Routes"""
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """ Return a list of all prcp names"""
    """Return the JSON representation of your dictionary"""
    recent_date = (
        session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    )
    date_year_ago = dt.datetime.strptime(recent_date, "%Y-%m-%d") - dt.timedelta(
        days=365
    )

    prec_scores = (
        session.query(Measurement.date, Measurement.prcp)
        .filter(Measurement.date >= date_year_ago)
        .order_by(Measurement.date)
        .all()
    )
    all_prcp =[]
    for score in prec_scores:
       prcp_dict = {}
       prcp_dict ["date"] = score[0]
       prcp_dict ["prcp"] = score[1]
       all_prcp.append(prcp_dict)
    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    """ Return a JSON list of stations from the dataset"""
    all_station = session.query(Measurement.station).group_by(Measurement.station).all()
    station_list = list(np.ravel(all_station))#ravel(returns contiguous flattened array)
    print("Statioins list:")
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the previous year"""
    recent_date = (
        session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    )
    date_year_ago = dt.datetime.strptime(recent_date, "%Y-%m-%d") - dt.timedelta(
        days=365
    )

    temp_obs = (
        session.query(Measurement.date, Measurement.tobs)
        .filter(Measurement.date >= date_year_ago)
        .order_by(Measurement.date)
        .all()
    )
    all_tobs =[]
    for tob in temp_obs:
        tobs_dict ={}
        tobs_dict["date"] = tob[0]
        tobs_dict["tobs"] = tob[1]
        all_tobs.append(tobs_dict)
    print("Temperature results for all stations")

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def calc_temp_start(start):
    """"Return a JSON list of The `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date. """
    start_date = trip_start_date = dt.date(2017, 7, 7)
    end_date = trip_end_date = dt.date(2017, 7, 22)
    select = [
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs),
    ]
    temp_result_start = (
        session.query(*select).filter(Measurement.date >= start_date).all()
    )
    print("Calculated temp for the start date")

    return jsonify(temp_result_start)


@app.route("/api/v1.0/<start>/<end>")
def calc_temp_start_end(start, end):
    """Return a JSON list of The `TMIN`, `TAVG`, and `TMAX` for the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive."""
    start_date = trip_start_date = dt.date(2017, 7, 7)
    end_date = trip_end_date = dt.date(2017, 7, 22)
    select = [
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs),
    ]
    temp_result_start_end = (
        session.query(*select)
        .filter(Measurement.date >= start_date)
        .filter(Measurement.date <= end_date)
        .all()
    )

    print("Calculated temp for the start date & end date")
    all_results = list(np.ravel(temp_result_start_end ))
    return jsonify(all_results)

if __name__ == "__main__":
    app.run(debug=True)   