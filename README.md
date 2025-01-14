# Crime Data Exploration

## Overview

This project explores crime data, focusing on crime types, locations, victim demographics, and trends over time. The dataset contains various features related to crimes, including the crime description, location, victim details, and the date/time of the crime. By analyzing this data, the goal is to uncover insights that can aid in understanding crime patterns and inform decision-making.

## Project Structure

Crime-Data-Exploration/ │ ├── crime_data.csv # Raw crime dataset ├── analysis.py # Python script for data cleaning, analysis, and visualization ├── README.md # Project documentation └── requirements.txt # Required Python libraries

## Features and Analysis

The project includes the following steps and analyses:

1. **Data Cleaning and Preprocessing**
    - Dropped irrelevant columns.
    - Handled missing values and data types.
    - Removed duplicates.
    - Converted time-related columns into the appropriate format.

2. **Exploratory Data Analysis (EDA)**
    - Descriptive statistics (mean, median, mode, etc.) for numerical features.
    - Visualizations:
      - Top 10 Crimes by Crime Description
      - Crime Distribution by Area
      - Crime Distribution by Year
      - Victim Age Distribution (Categorized)
      - Victim Age vs. Crime Type (Boxplot)
    - Correlation analysis using a heatmap.

3. **Hypothesis Testing**
    - ANOVA test to assess if there are significant differences in victim age by area.
    - Chi-Square test for association between crime type and case status.

4. **Time Series Analysis**
    - Trends in crimes over months, visualized as a time series plot.

5. **Outlier Detection**
    - Z-score analysis to detect outliers in victim age.

## Getting Started

### Prerequisites

To run this project, you will need Python installed along with the following libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scipy

You can install the required libraries by running:

pip install -r requirements.txt


### Running the Project

1. Clone the repository:

git clone https://github.com/yourusername/Crime-Data-Exploration.git

2. Place the `crime_data.csv` file in the project directory.
3. Run the Python script:

python analysis.py


The script will output various results, including statistical summaries, visualizations, and hypothesis test results.

## Visualizations

### 1. Top 10 Crimes by Crime Description
This bar plot shows the top 10 most common crime descriptions.

### 2. Crime Distribution by Area
This bar plot highlights the areas with the highest number of reported crimes.

### 3. Crime Distribution by Year
A line plot shows how the number of crimes changes over time, by year.

### 4. Victim Age Distribution
A histogram categorizes victims by age group and shows the distribution of victim ages.

### 5. Victim Age vs. Crime Type
A boxplot to compare the victim age distribution across different crime types.

## Analysis Results

- **Descriptive Statistics**: Summary statistics such as mean, median, mode, and standard deviation for victim age.
- **Correlation Heatmap**: Visualizes the relationships between numerical variables in the dataset.
- **Hypothesis Testing**: Results from the ANOVA and Chi-Square tests.
- **Time Series Plot**: Shows monthly crime trends over the years.
- **Outlier Detection**: Identifies outliers in the victim age data based on the Z-score.

## Conclusion

This project demonstrates how to explore and analyze crime data, uncover patterns, and perform statistical tests. By exploring various aspects of crime data, it’s possible to gain insights that can be useful for policy-making, law enforcement, and urban planning.

## Future Work

- Investigating additional correlations with external datasets (e.g., socio-economic data).
- Predictive modeling to forecast crime trends.
- Incorporating more granular time analysis, such as hourly or weekly crime patterns.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


