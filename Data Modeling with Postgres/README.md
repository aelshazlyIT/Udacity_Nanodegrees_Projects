
# Data Modeling with Postgres

Sparkify, a music streaming startup, is looking for a data engineer to create a database schema and ETL pipline to assist the company in analyzing user data. In particular, the company is interested in understanding what songs users are listening to.

The objective of this project is to ingest the data provided by Sparkify and design a method of storage using a relational data model in Postgres.


# Overview
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


# Datasets:

## Song Dataset
metadata about a song and the artist of that song. Song data files are partitioned by the first 3 letters of each track's song id.

Sample Record :
```
{
  "num_songs": 1,
  "artist_id": "ARJIE2Y1187B994AB7",
  "artist_latitude": null,
  "artist_longitude": null,
  "artist_location": "",
  "artist_name": "Line Renaud",
  "song_id": "SOUPIRU12A6D4FA1E1",
  "title": "Der Kleine Dompfaff",
  "duration": 152.92036,
  "year": 0
}
```

## Log Dataset
simulation of activity logs from Sparkify app. Log files are partitioned by year and month.
Sample Record :
```
{
  "artist": "Pavement",
  "auth": "Logged In",
  "firstName": "Sylvie",
  "gender": "F",
  "itemInSession": 0,
  "lastName": "Cruz",
  "length": 99.16036,
  "level": "free",
  "location": "Washington-Arlington-Alexandria, DC-VA-MD-WV",
  "method": "PUT",
  "page": "NextSong",
  "registration": 1540266185796.0,
  "sessionId": 345,
  "song": "Mercy:The Laundromat",
  "status": 200,
  "ts": 1541990258796,
  "userAgent": "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4\"",
  "userId": "10"
}
```


# Schema

This project implements a star schema. songplays is the fact table in the data model, while users,songs,artists, and time are all dimensional tables.


## Fact Table 
**songplays** - records in log data associated with song plays i.e. records with page `NextSong`

```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

1    2018-11-29 00:00:57.796000    73    paid    -    -    954    Tampa-St. Petersburg-Clearwater, FL
```

## Dimension Tables
**users**  - users in the app
```
user_id, first_name, last_name, gender, level

79    James    Martin    M    free

```
**songs**  - songs in music database
```
song_id, title, artist_id, year, duration

SOFFKZS12AB017F194    A Higher Place (Album Version)    ARBEBBY1187B9B43DB    1994    236.17261
```
**artists**  - artists in music database
```
artist_id, name, location, latitude, longitude

ARNNKDK1187B98BBD5    Jinx    Zagreb Croatia    45.80726    15.9676
```
**time**  - timestamps of records in  **songplays**  broken down into specific units
```
start_time, hour, day, week, month, year, weekday

2018-11-29 00:01:30.796000    0    29    48    11    2018    3
```



## Repository Structure

- data folder - includes song_data and log_data; raw jason files provided by Sparkify.
- etl.ipynb - environment for designing and testing ETL process.
- etl.py - contains all ETL procedures.
- create_tables.py - creates the database and tables.
- sql_queries.py - contains DDL/DML required for the ETL process.
- test.ipynb - runs a series of test queries to ensure that tables are present and data is flowing through the ETL process as expected.


# to run the code:

- create_tables.py: Clean previous schema and creates tables.
- sql_queries.py: All queries used in the ETL pipeline.
- etl.py: Read JSON logs and JSON metadata and load the data into generated tables.


