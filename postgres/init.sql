CREATE TABLE data (
  city_name VARCHAR,
  start_timestamp TIMESTAMP(3) with TIME ZONE,
  end_timestamp TIMESTAMP(3) with TIME ZONE,
  num_observations_in_window INTEGER,
  min_temperature_in_window NUMERIC(6,2),
  max_temperature_in_window NUMERIC(6,2),
  avg_temperature_in_window NUMERIC(6,2),
  wind_speed NUMERIC(6,2),
  humidity NUMERIC(6,2),
  temp_difference NUMERIC(6,2),
  humidity_difference NUMERIC(6,2),
  wind_speed_difference NUMERIC(6,2),
  PRIMARY KEY (city_name, start_timestamp)


);