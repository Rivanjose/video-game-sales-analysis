# Video-game-sales-analysis
Python project analyzing video game sales data.
# Video Game Sales Analysis

## Project Title
**Video Game Sales Analysis Using Python**

## Short Description
This project analyzes video game sales data using Python and Pandas. It extracts and processes sales records for games released before and after 2005.

## Getting Started

### Prerequisites
- Python 3.x
- Pandas library

### Installing
1. Clone repository to local machine:
   ```sh
   git clone https://github.com/Rivanjose/video-game-sales-analysis.git
Navigate to the project directory:
   ```sh
   cd video-game-sales-analysis
   ```
 Install the required Python packages:
   ```sh
   pip install pandas

### Running the Tests
=================
To verify that the script functions correctly, follow these steps:
1. Ensure you have a sample dataset (CSV file) containing video game sales data.
2. Modify the script to read from the dataset if necessary.
3. Execute the script using the following command:
   ```sh
   python video_game_sales_analysis.py
   ```
4. Validate the output to ensure:
   - The dataset is loaded correctly.
   - The filtering criteria (games released after 2005) work as expected.
   - No errors occur during execution.
   - 
### Explaining each steps:

1.import pandas as pd
  import pymysql
  from sqlalchemy import create_engine
  import matplotlib.pyplot as plt
  import seaborn as sns

DataFrames, or structured data, can be handled and analyzed using pandas.
A library called pymysql is used to link Python to a MySQL database.
Creating a connection to the MySQL database is done with sqlalchemy.create_engine.
Seaborn and matplotlib.pyplot are used to visualize data.

2. 


### Break down into end-to-end tests

These tests confirm that the functions for data extraction, processing, and filtering operate as intended.

Examples of Tests:
1. Open a CSV file containing sales information for video games.
2. After 2005, filter games were released.
3. Determine the overall sales for every area.
4. Present a prepared output of the results.


## Deployment
To use this script in a production environment:
- Ensure the dataset is securely stored and accessible.
- Optimize data processing if handling large datasets.
- Consider automating the script execution if frequent updates are required.

## Author
**Rivan Jose**  
Data Analytics Student, Durham College

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments
Special thanks to Durham College for providing access to real-world datasets and fostering a data-driven learning environment.

