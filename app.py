import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
session = Session(engine)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    results = results[0]
    year_ago = dt.datetime.strptime(results, "%Y-%m-%d")- dt.timedelta(days=366)
    results1=session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>=year_ago).all()
    
    #returnig the dict in a jsonified formart
    prcp_results= dict(results1)
    return jsonify(prcp_results)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Measurement.station).group_by(Measurement.station).all()
    station_list = list(results)
    
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    results = results[0]
    year_ago = dt.datetime.strptime(results, "%Y-%m-%d")- dt.timedelta(days=366)
    query = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= year_ago, Measurement.station == 'USC00519281').order_by(Measurement.date).all()
    
    tobs_dict = dict(query)
    return jsonify(tobs_dict)

@app.route("/api/v1.0/<start>")
def trip1(start):

    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    year_ago = start_date - dt.timedelta(days=365)
    #end is the last day that we have data for 
    end =  dt.date(2017, 8, 23)
    trip_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).filter(Measurement.station == 'USC00519281').all()
    trip = list(np.ravel(trip_data))
    return jsonify(trip)

@app.route("/api/v1.0/<start>/<end>")
def trip2(start,end):

  # go back one year from start/end date and get Min/Avg/Max temp     
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    trip_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).filter(Measurement.station == 'USC00519281').all()
    trip = list(np.ravel(trip_data))
    return jsonify(trip)

if __name__ == '__main__':
    app.run(debug=True)
