CREATE TABLE fireRed1 (
  objectid INTEGER,
  fod_id INTEGER,
  fpa_id VARCHAR(50),
  source_system_type VARCHAR(50),
  source_system VARCHAR(50),
  nwcg_reporting_agency VARCHAR(50),
  nwcg_reporting_unit_id VARCHAR(50),
  nwcg_reporting_unit_name VARCHAR(50),
  source_reporting_unit INTEGER,
  source_reporting_unit_name VARCHAR(50),
  local_fire_report_id INTEGER,
  local_incident_id VARCHAR(50),
  fire_code VARCHAR(50),
  fire_name VARCHAR(50),
  ics_209_incident_number VARCHAR(50),
  ics_209_name VARCHAR(50),
  mtbs_id VARCHAR(50),
  mtbs_fire_name VARCHAR(50),
  complex_name VARCHAR(50),
  fire_year INTEGER,
  discovery_date FLOAT,
  discovery_doy FLOAT,
  discovery_time INTEGER,
  stat_cause_code FLOAT,
  stat_cause_descr VARCHAR(50),
  cont_date FLOAT,
  cont_doy FLOAT,
  cont_time INTEGER,
  fire_size FLOAT,
  fire_size_class VARCHAR(50),
  latitude FLOAT,
  longitude FLOAT,
  owner_code FLOAT,
  owner_descr VARCHAR(50),
  state VARCHAR(50),
  county FLOAT,
  fips_code FLOAT,
  fips_name VARCHAR(50),
  shape VARCHAR(250) 
);
--------

drop table firered1;  -- drop the table

copy firered1
from 's3://landing-zone1/firecsv_small.csv' 
iam_role 'arn:aws:iam::931462350408:role/lab5_test1'
region 'us-east-2'
IGNOREHEADER 1
csv
null as '\000'; --- copy data from s3 into redshift

select * from firered1 limit 10; -- see our data
-----------------------
select * from stl_load_errors;
