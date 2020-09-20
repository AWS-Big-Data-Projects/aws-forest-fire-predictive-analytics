SELECT *  FROM athena_crawler_2.landing_zone1 limit 10;
SELECT count(fod_id) as count, state  FROM athena_crawler_2.landing_zone1 GROUP BY state;

select max(count) as c, state from
(SELECT state,count(fod_id) as count FROM athena_crawler_2.landing_zone1 GROUP  BY state order by count desc) group by state order by c desc limit 1  ;

select * from
(SELECT state,count(fod_id) as count FROM athena_crawler_2.landing_zone1 GROUP  BY state order by count limit 1) where state <> 'STATE';

select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2.landing_zone1 where state='CO' ;
select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2.landing_zone1 where state='AZ' ;
select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2.landing_zone1 where state='FL' ;
select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2.landing_zone1 where state='TX' ;


select fire_size from athena_crawler_2.landing_zone1 where state='AZ' ;
select fire_size from athena_crawler_2.landing_zone1 where state='CA’ ;
select fire_size from athena_crawler_2.landing_zone1 where state='FL’ ;
select fire_size from athena_crawler_2.landing_zone1 where state='CO’;



-- From reduced table
SELECT * FROM athena_crawler_2_reduced.etl_output;

select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2_reduced.etl_output where state='TX' ;
select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2_reduced.etl_output where state='CO' ;
select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2_reduced.etl_output where state='AZ' ;
select max(stat_cause_descr) as cause,count(stat_cause_descr) as number from athena_crawler_2_reduced.etl_output where state='FL' ;

select fire_size from athena_crawler_2_reduced.etl_output where state='AZ' ;
select fire_size from athena_crawler_2_reduced.etl_output where state='CA’ ;
select fire_size from athena_crawler_2_reduced.etl_output where state='FL’ ;
select fire_size from athena_crawler_2_reduced.etl_output where state='CO’;








