

# Kafka Producer
Using the Kafka Topics CLI, topics appear for arrivals on each train line in addition to the turnstiles for each of those stations.

Using the Kafka Topics CLI, messages continuously appear for each station on the train line, for both arrivals and turnstile actions.

Using the Schema Registry API, a schema is visible for arrivals and turnstile events.

# Kafka Consumer
Stations, status, and weather data appear and update in the Transit Status UI.

Good job setting a proper default offset_reset config.

All Blue, Green, and Red Line stations appear in the Transit Status UI.

# Kafka REST Proxy
Using the kafka-console-consumer, weather messages are visible in the weather topic and are regularly produced as the simulation runs.

Using the Kafka Schema Registry REST API, a schema is defined for the weather topic.

You correctly set up the status as an enum type.
Screen Shot 2021-01-26 at 6.52.50 PM.png

# Kafka Connect
Using the kafka-console-consumer, all stations defined in Postgres are visible in the stations topic.

Using the Kafka Connect REST API, the Kafka Connect configuration is configured to use JSON for both key and values.

Using the Schema Registry REST API, the schemas for stations key and value are visible.

Using the Kafka Connect REST API, the Kafka Connect configuration uses an incrementing ID, and the ID is configured to be stop_id.

# Faust Streams
A consumer group for Faust is created on the Kafka Connect Stations topic.

Data is ingested in the Station format and is then transformed into the TransformedStation format.

A topic is present in Kafka with the output topic name the student supplied. Inspecting messages in the topic, every station ID is represented.

# KSQL
Using the KSQL CLI, turnstile data is visible in the table TURNSTILE.

Using the KSQL CLI, verify that station IDs have an associated count column.
