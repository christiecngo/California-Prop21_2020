# ALDUCHWE - Prop 21: Predicting Homeless Population Based on Rent Control
Training sklearn models to build 2 models (1 for a rent controlled city, 1 for for a city without rent control) with features -- median income, unemployment rate, crime numbers, and population count -- to predict homeless population of cities with similar policies. 

## Layout
Datasets of each feature for the 4 featured cities are collected within the "data" branch. All other files, including modeling and visualization code, are found in the master branch.

## Abbreviations used within datasets
	SF- San Francisco
	SD- San Diego
	SJ - San Jose
	POP - (city's) population
	UNEMP - (city's) unemployment

## Data Sources
Datasets were last modified on 20200927. All files are in the formats: [.CSV, .xlsx, and .py]

Population measured in counts of people based on the U.S. Census Bureau. Unemployment rate of cities were chosen based on the unemployment percentage of cities on the 1st day of the first month for each year recorded. Crime numbers were measured as a crime recording made by city/police reports. There are discrepancies between whether the sources recorded number of actual crimes or the number of crimes simply reported. Median income is added as an average of median incomes for cities annually in U.S. dollars. 

### Homeless Population 

All homeless numbers were determined by PIT counts for each CoC published by the [hudexchange organization](https://www.hudexchange.info/programs/coc/coc-homeless-populations-and-subpopulations-reports) in the selected cities: San Francisco, San Diego, San Jose, and Fresno.

### Crime Numbers

### Unemployment Rate

### City Population

### Median Income

## Contributing
JupyterNotebook("datascienceprop21.py") can be ran on an external server for visualization of the model results and training code. Datasets can be downloaded as EXCEL files. Data collection is from 2005-2018, and additional variable features can easily be added to training dataframe. Code written for checking collinearity and OLS results are adaptable to additional independent variables as well. Any city chosen with data for each feature can be used to predict the homeless population using the models.

	

## Contact
	Christie Ngo: ccngo@ucdavis.edu
	
	Dustin Nguyen: dusnguyen@ucdavis.edu
	
	Alvin Tang: alqtang@ucdavis.edu
	
	Wesley Tat: wrtat@ucdavis.edu
	
