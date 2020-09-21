
CREATE TABLE firered_reduced2 (
  fire_year INTEGER,
  stat_cause_descr VARCHAR(50),
  fire_size FLOAT,
  fire_size_class VARCHAR(50),
  latitude FLOAT,
  longitude FLOAT,
  state VARCHAR(50),
  county FLOAT,
  discovery_date FLOAT,
  cont_date FLOAT
);
--------

drop table firered_reduced2;  -- drop the table

copy firered_reduced2
from 's3://staging-area1/etl_output/run-1556584724898-part-r-00000' 
iam_role 'arn:aws:iam::931462350408:role/lab5_test1'
region 'us-east-2'
IGNOREHEADER 1
csv
null as '\000'; --- copy data from s3 into redshift

select * from firered_reduced2 limit 10; -- see our data
-----------------------
select * from stl_load_errors;

---------
	fire_year
	stat_cause_descr
	fire_size
	fire_size_class
	latitude
	longitude
	state
	county
	discovery_date
	cont_date
