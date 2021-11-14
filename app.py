#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import flask dependencies
from flask import Flask, jsonify

#Set up database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect the database to the classes
Base = automap_base()

#Reflect the tables
Base.prepare(engine, reflect=True)

#Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database.
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Set the welcome route at the base
@app.route("/")

# Create a welcome() function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')

# Create new route for precipitation
@app.route("/api/v1.0/precipitation")

# Create precipitation function
def precipitation():
    # Calculate date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # Create a dicitonary with the date as the key and the precipitation as the value.
    # Then "jsonify" the dictionary to convert it to a JSON file.
    precip = {date: prcp for date, prcp in precipitation} 
    return jsonify(precip)

# Create a new route for stations
@app.route("/api/v1.0/stations")

# Create function to get stations
def stations():
#Get all the stations in our database
    results = session.query(Station.station).all()
    # Use function np.ravel(results) to unravel results, then convert results to a list with list()
    stations = list(np.ravel(results))
    # Then "jsonify" the dictionary to convert it to a JSON file. To return list as JSON need to add stations=stations.
    return jsonify(stations=stations)

# Create a new route for temperature observations
@app.route("/api/v1.0/tobs")

# Create a function to get temperature observations
def temp_monthly():
    # Calculate the date one year ago from the last date in the database.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Query the primary station for all the temp observations from the previous year.
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    # Use function np.ravel(results) to unravel results, then convert results to a list with list()
    temps = list(np.ravel(results))
    # Then "jsonify" the dictionary to convert it to a JSON file. To return list as JSON need to add temps=temps.
    return jsonify(temps=temps)

# Create Statistics Route
# Create starting and ending routes
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a stats() function with a start and end parameter. Set to none initially.
def stats(start=None, end=None):
    # Create a list called sel[] to hold min, avg and max temps.
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Determine start and end dates. The asterisk indicates there will be multiple results (min, avg, max)
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    # Calculate min, avg and max temps.
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

