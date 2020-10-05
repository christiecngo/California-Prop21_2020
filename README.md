# ALDUCHWE - Prop 21: Predicting Homeless Population Based on Rent Control
Training sklearn models to build 2 models (1 for a rent controlled city, 1 for for a city without rent control) with features -- median income, unemployment rate, crime numbers, and population count -- to predict homeless population of cities with similar policies. 

## Layout
Datasets of each feature for the 4 featured cities are collected within the "data" branch. All other files, including modeling and visualization code, are found in the master branch.

## Abbreviations/Conventions
	SF- San Francisco
	SD- San Diego
	SJ - San Jose
	POP - (city's) population
	UNEMP - (city's) unemployment

* Dataset files for each city should include the abbreviated city's name in title.

## Data Sources
Datasets were last modified on 20200927. All files are in the formats: [.CSV, .xlsx, and .py]

Population measured in counts of people based on the U.S. Census Bureau. Unemployment rate of cities were chosen based on the unemployment percentage of cities on the 1st day of the first month for each year recorded. Crime numbers were measured as a crime recording made by city/police reports. There are discrepancies between whether the sources recorded number of actual crimes or the number of crimes simply reported. Median income is added as an average of median incomes for cities annually in U.S. dollars. 

### Homeless Population 

All homeless numbers were determined by PIT counts for each CoC published by the [HUD Exchange](https://www.hudexchange.info/programs/coc/coc-homeless-populations-and-subpopulations-reports) in the selected cities: San Francisco, San Diego, San Jose, and Fresno.

### Crime Numbers
Different crime sources were used for each city chosen. 

* [Data SF](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry) provided numbers of crimes reported for SF from 2005-2018 in two different sets.
* [San Diego's Government Website](https://www.sandiego.gov/sites/default/files/crime-actuals1950-2019.pdf) listed actual total number of crimes for years within the last several decades.
* [Santa Clara's Government Report on Crime Trends in California](https://www.sccgov.org/sites/da/prosecution/DistrictAttorneyDepartments/Documents/CSU%20Reports/10-Year%20Combined%20CA%20Crime%20Stat%20Report.pdf) shows the number of each type of crime in San Jose over the decade 2006-2017. Total number of crimes were summed up using EXCEl (total homicide + total aggravated assault + total vehicle theft + burglary (residence) + burglary (Non-residence) + total robberies + larceny) for years 2005-2009.
For years [2010-2018](http://www.sjpd.org/crimestats/annual_crimestats.html), reports from the SJ Police Department was used.
* [Fresno Crime Statistics](https://www.macrotrends.net/cities/us/ca/fresno/crime-rate-statistics) from macrotrends show Fresno crimes per 100,000 people. Total crime was calculated using Fresno's population each year. 


### Unemployment Rate
FRED Economic Data published the unemployment rate for counties that the cities are in:

* [San Francisco County](https://fred.stlouisfed.org/series/CASANF0URN)
* [San Diego County](https://fred.stlouisfed.org/series/CASAND5URN)
* [Santa Clara County](https://fred.stlouisfed.org/series/CASANT5URN)
* [Fresno County](https://fred.stlouisfed.org/series/CAFRES9URN)


### City Population
City population numbers came from the Census Bureau:

* [San Francisco](https://www.census.gov/quickfacts/fact/table/sanfranciscocitycalifornia,US/PST045219)
* [San Diego](https://www.census.gov/quickfacts/fact/table/sandiegocitycalifornia,US/PST045219)
* [San Jose](https://www.census.gov/quickfacts/fact/table/sanjosecitycalifornia,US/PST045219)
* [Fresno](https://www.census.gov/quickfacts/fact/table/fresnocitycalifornia,US/PST045219)

### Median Income

FRED Economic Data had estimated median income for each county that our selected cities were in:
* [San Francisco County](https://fred.stlouisfed.org/series/MHICA06075A052NCEN)
* [San Diego County](https://fred.stlouisfed.org/series/MHICA06073A052NCEN)
* [Fresno County](https://fred.stlouisfed.org/series/CAFRES9URN)

* [San Jose](https://www.deptofnumbers.com/income/california/san-jose/) had data for the city itself

## Contributing
JupyterNotebook("datascienceprop21.py") can be ran on an external server for visualization of the model results and training code. Datasets can be downloaded as EXCEL files. Data collection is from 2005-2018, and additional variable features can easily be added to training dataframe. Code written for checking collinearity and OLS results are adaptable to additional independent variables as well. Any city chosen with data for each feature can be used to predict the homeless population using the models.

	

## Contact
	Christie Ngo: ccngo@ucdavis.edu
	
	Dustin Nguyen: dusnguyen@ucdavis.edu
	
	Alvin Tang: alqtang@ucdavis.edu
	
	Wesley Tat: wrtat@ucdavis.edu
	
