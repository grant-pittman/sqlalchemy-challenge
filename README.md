# SQLAlchemy Homework - Surfs Up <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [Background](#background)
- [Climate Analysis and Exploration](#climate-analysis-and-exploration)
- [Climate App](#climate-app)

## Background

In this challenge, I am analyzing climate data for Honolulu, Hawaii.

## Climate Analysis and Exploration

The code for the Climate and Analysis and Exploration can be seen in the file climate_starter.ipynb
Here, I did multiple analyses.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

* Listed the stations and observation counts in descending order.

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

* Filtered by the station with the highest number of observations.

* Plot the results as a histogram with `bins=12`.

## Climate App

Code for the climate app can be found under app.py.  Enter "python app.py" into a terminal.  You then will go to [http://127.0.0.5000/](http://127.00.5000/) to start the results.

### Flask

* Designed a Flask API based on the queries from above.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data.
  
  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

