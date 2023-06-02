use role sysadmin;

use database tutorial_db;
CREATE OR REPLACE TABLE sales(emp_id INTEGER, year INTEGER, revenue DECIMAL(10,2));

INSERT INTO sales VALUES 
    (0, 2010, 1000), 
    (0, 2011, 1500), 
    (0, 2012, 500), 
    (0, 2013, 750);
INSERT INTO sales VALUES 
    (1, 2010, 10000), 
    (1, 2011, 12500), 
    (1, 2012, 15000), 
    (1, 2013, 20000);
INSERT INTO sales VALUES 
    (2, 2012, 500), 
    (2, 2013, 800);

select * from sales;
SELECT emp_id, year, revenue, 
       revenue - LAG(revenue, 1, 0) OVER (PARTITION BY emp_id ORDER BY year) AS diff_to_prev 
    FROM sales 
    ORDER BY emp_id, year;


    SELECT distinct package_name
FROM   information_schema.packages 
WHERE  language = 'python' ;