CREATE DATABASE google_playstore_db;
USE google_playstore_db;

SHOW TABLES;

RENAME TABLE `googleplaystore`
TO playstore;

SELECT * FROM playstore ;

DESC playstore_clean;

SELECT * FROM playstore_clean LIMIT 10;

SELECT COUNT(*) FROM playstore_clean;

-- Count total number of applications
SELECT COUNT(*) AS Total_Apps
FROM playstore_clean;

-- Count applications in each category

-- Calculate average rating for each category
SELECT Category,
ROUND(AVG(Rating),2) AS Average_Rating
FROM playstore_clean
GROUP BY Category
ORDER BY Average_Rating DESC;

-- Calculate total installs for each category
SELECT Category,
SUM(Installs) AS Total_Installs
FROM playstore_clean
GROUP BY Category
ORDER BY Total_Installs DESC;

-- Compare average rating of Free and Paid apps
SELECT Type,
ROUND(AVG(Rating),2) AS Average_Rating
FROM playstore_clean
GROUP BY Type;

-- Calculate average rating by content rating
SELECT `Content Rating`,
ROUND(AVG(Rating),2) AS Average_Rating
FROM playstore_clean
GROUP BY `Content Rating`;

-- Display top 10 most installed applications
SELECT App,
Installs
FROM playstore_clean
ORDER BY Installs DESC
LIMIT 10;

-- Calculate average application price
SELECT ROUND(AVG(Price),2) AS Average_Price
FROM playstore_clean;

-- Display recently updated applications
SELECT App,
`Last Updated`
FROM playstore_clean
ORDER BY `Last Updated` DESC;

-- Count applications updated every year
SELECT Year,
COUNT(*) AS Total_Apps
FROM playstore_clean
GROUP BY Year
ORDER BY Year;



