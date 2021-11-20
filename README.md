# Surfs_Up Analysis

## Project Overview

The purpose of the project is to analyze weather data in Oahu to determine if the weather would affect the success of a potential business selling surfboards and ice cream. W. Avy is an investor who is very interested in financing the project, but wants to ensure that the weather analysis will show whether this is a good project to invest in.

## Tools Used
 
 - Python
 - Pandas functions and methods
 - SQLAlchemy

## Process

 - Step 1: Write a query to filter all the temperatures for the months of June and December for all years in the database.
 - Step 2: Convert the June and December temperatures to a list.
 - Step 3: Create a DataFrame from the list of temperatures for the months of June and December.
 - Step 4: Generate the summary statistics for the June and December temperatures DataFrame.

## June Temperature Results

Temperatures for the month of June from 2010 through 2017 show that the average temperature is 74.9. The minimum recorded during this date range is 64 degrees, and the maximum recorded is 85 degrees.

![June_temps.png](/Resources/June_temps.png)

## December Temperature Results

Temperatures for the month of December from 2010 through 2016 show that the average temperature is 71.0. The minimum recorded during this date range is 56 degrees, and the maximum recorded is 83 degrees. The data for December only goes through 2016, while the data for June contains an additional year's data (2017).

![December_temps.png](/Resources/December_temps.png)

## Analysis

The difference in the average temperatures for the months of June and December is negligible. There is only a four-degree difference in average temperatures (June: 74.9, December: 71.0). The minimum temperatures are also close (June: 64, December, 56). The maximum temperatures differ by only two degrees (June: 85, December, 83). 

Overall, the climate on Oahu appears to maintain a relatively steady temperature that is neither too hot nor too cold. The analysis of the weather indicates that this would be an ideal location to open a surfboard and ice cream Store.

## Additional Queries

Other queries that would provide additional data for analysis are June and December precipitation amounts:

### June Precipitation

### December Precipitation
The average precipitation for June from 2010 through 2017 is .13 inches, while the minimum recorded is 0 and the maximum is 4.43 inches.

![June_prec.png](/Resources/June_prec.png)

The average precipitation for December from 2010 through 2016 is .21 inches, while the minimum recorded is 0 and the maximum is 6.42 inches.

![December_prec.png](/Resources/December_prec.png)

The precipitation analysis shows that there is usually little difference between the precipitation in June and December, although December seems to be a bit more rainy than June. Overall, however, the skies seem to be perfect for this new venture.




