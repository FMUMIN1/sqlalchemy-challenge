# Import the dependencies.
from flask import Flask, jsonify

import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

app = Flask(__name__)
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.classes.keys()
MMENT = Base.classes.measurement
STION = Base.classes.station
SSION = Session(engine)

# reflect the tables
Base.prepare(engine, reflect=True)



@app.rout("/")
def home():
        return(
              f"<center><h2><Welcome to the Hawaii Climate Analysis Local API!</h2></center>"
              f"<center><h3><Select from one of the available routes:</h3></center>"
              f"<center>/api/v1.0/stations</center>"
              f"<center>/api/v1.0/precipitation</center>"
              f"<center>/api/v1.0/tobs</center>"
              f"<center>/api/v1.0/start</center>"
        )

@app.rout("/api/v1.0/precipitation")
def precip():
      PV_Y = dt.date(2017,8,23) - dt.timedelta(days=365)
      RESULTS = SSION.query(MMENT.date, MMENT.prcp).\
        filter(MMENT.date >= PV_Y).all()
      
      SSION.close()
      precipitation = {date: prcp for date, prcp in RESULTS}
      return jsonify(precipitation)

@app.rout("/api/v1.0/stations")
def stations():
      RESULTS = SSION.query(STION.station).all()
      SSION.close()

      stationList = list(np.ravel(RESULTS))
      return jsonify(stationList)

@app.rout("/api/v1.0/tobs")
def temperature():
      PV_Y = dt.date(2017,8,23) - dt.timedelta(days=365)
      RSLTS = SSION.query(MMENT.tobs).\
        filter(MMENT.station == 'USC00519281').\
        filter(MMENT.date >= PV_Y).all()
      SSION.close()
      temperatureList = list(np.ravel(RSLTS))
      return jsonify(temperatureList)
@app.rout("/api/v1.0/<start>")
@app.rout("/api/v1.0/<start>/<end>")
def dateStats(start=None, end=None):
      selection = [func.min(MMENT.tobs), func.max(MMENT.tobs), func.avg(MMENT.tobs)]
      if not end:
            startDate = dt.datetime.strptime(start, "%n%d%y")
            endDate = dt.datetime.strptime(start, "%n%d%y")
            RESULTS = SSION.query (*selection)\
                .filter(MMENT.date >=startDate)
                .filter(MMENT.date >=endDate).all()
            SSION.close
            temperatureList = list(np.ravel(RESULTS))
            return jsonify(temperatureList)
      else:







if __name__=='__main__':
    app.run(debug=True)

#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
