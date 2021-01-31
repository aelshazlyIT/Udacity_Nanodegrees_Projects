# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
    (
        songplay_id                                    SERIAL, 
        start_time      TIMESTAMP REFERENCES time(start_time), 
        user_id        INT NOT NULL REFERENCES users(user_id), 
        level                                         VARCHAR, 
        song_id             VARCHAR REFERENCES songs(song_id), 
        artist_id        VARCHAR REFERENCES artists(artist_id), 
        session_id                                        INT, 
        location                                      VARCHAR, 
        user_agent                                    VARCHAR,
        PRIMARY KEY(songplay_id)
    );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
    (
        user_id                   INT, 
        first_name   VARCHAR NOT NULL, 
        last_name    VARCHAR NOT NULL, 
        gender                VARCHAR, 
        level                 VARCHAR,
        PRIMARY KEY(user_id)
        
    );
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs 
    (
        song_id                             VARCHAR, 
        title                      VARCHAR NOT NULL, 
        artist_id                  VARCHAR NOT NULL, 
        year                                    INT, 
        duration                     FLOAT NOT NULL,
        PRIMARY KEY(song_id)
    );
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists 
    (
        artist_id                     VARCHAR, 
        artist_name                   VARCHAR, 
        artist_location               VARCHAR, 
        artist_latitude                 FLOAT, 
        artist_longitude                FLOAT,
        PRIMARY KEY(artist_id)
    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time 
    (
        start_time               TIMESTAMP, 
        hour                           INT, 
        day                            INT, 
        week                           INT, 
        month                          INT, 
        year                           INT, 
        weekday                        INT,
        PRIMARY KEY(start_time)
    );
""")

# INSERT RECORDS

songplay_table_insert = (
    """
    INSERT INTO songplays (
        start_time, 
        user_id, 
        level, 
        song_id, 
        artist_id, 
        session_id, 
        location, 
        user_agent
        ) 
 VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
 """)

user_table_insert = (
    """
    INSERT INTO users (
        user_id, 
        first_name, 
        last_name, 
        gender, 
        level
        ) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (user_id) 
DO UPDATE SET 
    first_name=users.first_name, 
    last_name=users.last_name, 
    gender=users.gender, 
    level=users.level 
""")

song_table_insert = (
"""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration
    ) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) 
DO UPDATE SET 
    title=songs.title, 
    artist_id=songs.artist_id,
    year=songs.year, 
    duration=songs.duration 
""")

artist_table_insert = (
"""
INSERT INTO artists (
    artist_id, 
    artist_name, 
    artist_location, 
    artist_latitude, 
    artist_longitude
    ) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO UPDATE SET 
    artist_name=artists.artist_name, 
    artist_location=artists.artist_location, 
    artist_latitude=artists.artist_latitude,
    artist_longitude=artists.artist_longitude 
""")

time_table_insert = (
"""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday
    ) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) 
DO UPDATE SET 
    hour=time.hour, 
    day=time.day, 
    week=time.week, 
    month=time.month, 
    year=time.year, 
    weekday=time.weekday 
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id
FROM songs s join artists a on s.artist_id = a.artist_id
WHERE s.title = %s AND a.artist_name = %s AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [
    user_table_create, 
    artist_table_create, 
    time_table_create,
    song_table_create,
    songplay_table_create
]

drop_table_queries = [
    songplay_table_drop, 
    user_table_drop, 
    song_table_drop, 
    artist_table_drop, 
    time_table_drop
]