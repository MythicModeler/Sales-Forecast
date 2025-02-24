# Sales Forecasting and Markdown Analysis

## Overview
This project aims to forecast department-wide sales for each store over the next year while modeling the impact of promotional markdowns—especially during holiday weeks. The goal is to generate actionable recommendations that maximize business impact based on historical data.

## Data Description
This repository includes three CSV files (located in the `data/` folder):
- **sales_data_set.csv:** Contains weekly sales data for different stores and departments.
- **stores_data_set.csv:** Provides store-level details such as store IDs and other attributes.
- **features_data_set.csv:** Includes additional features such as holiday indicators, promotional events, and other factors that may affect sales.

## Current Progress
- **Exploratory Data Analysis (EDA):**  
  - Successfully loaded and visualized the raw data.
  - Implemented basic data parsing and date conversion.
  - Generated summary statistics and initial visualizations despite the messy data format.

## Project Roadmap / Next Steps
- **Data Cleaning:**  
  - Tidy up date formats, handle missing values, and standardize data.
- **Feature Engineering:**  
  - Create new features (e.g., extract month, week, holiday indicators) to improve model accuracy.
  - Merge datasets to form a comprehensive view of the data.
- **Forecasting Modeling:**  
  - Develop time series models (such as ARIMA or Prophet) to predict future sales.
  - Analyze the impact of promotional markdowns on sales.
- **Business Impact Analysis:**  
  - Translate model insights into actionable business strategies.
  - Prioritize recommendations based on potential ROI.

## Installation and Setup
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/MythicModeler/Sales-Forecast.git
    ```
2. **Navigate to the Project Directory:**
    ```bash
    cd holiday_sales
    ```
3. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv env
    ```
4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project
- **Exploratory Data Analysis (EDA):**  
  The EDA script (or notebook) is located in the `notebooks/` folder. To run it from the main directory:
    ```bash
    python notebooks/EDA.ipynb
    ```
  *Note:* If you prefer working in Jupyter Notebook, you can launch it from the main directory with:
    ```bash
    jupyter notebook
    ```

## Project Structure
holiday_sales/
├── data/                   # CSV data files
│   ├── sales_data_set.csv
│   ├── stores_data_set.csv
│   └── features_data_set.csv
├── env/                    # Virtual environment
├── notebooks/              # Jupyter notebooks and scripts
│   └── EDA.ipynb          # Exploratory Data Analysis notebook
├── README.md               # This file
└── requirements.txt        # Python dependencies

## Contributing
Contributions, suggestions, and feedback are welcome! If you have any ideas or improvements, please open an issue or submit a pull request.

## License
This project is open source. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- **Data Source:** [Kaggle](https://www.kaggle.com/)
- Special thanks to the contributors and the open-source community for providing tools and resources that made this project possible.
