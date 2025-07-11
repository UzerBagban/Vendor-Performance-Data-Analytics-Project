# Vendor-Performance-Data-Analytics-Project

This repository holds an end-to-end data analytics project on optimizing vendor performance. It illustrates a complete data pipeline, from raw data ingestion and exploratory data analysis to advanced statistical modeling, reporting, and interactive dashboarding. This project is intended to be a solid portfolio piece, with demonstrations of practical skills desired for a data analyst in real companies.


🚀 Project Overview

The main purpose of this project is to examine different elements of vendor performance, look for important trends, and offer actionable recommendations to increase profitability, optimize stock, and improve vendor relationships. Using a blend of Python to process and analyze data, SQLite to manage databases, and Power BI for visualization, the project offers a complete picture of the data analytics process.

This project directly answers typical issues encountered by future data analysts:

• Real-World Scenario: Solving a real-world business issue (vendor performance) that transcends theoretical practice.

• Skill Integration: Proving the smooth integration of SQL, Python, and Power BI into one complete project.

• Comprehensive Workflow: Complete data lifecycle from raw data to final recommendations and interactive dashboards.


✨ Features

• Automated Data Ingestion: Python script to import multiple CSV files into an SQLite database.

• Exploratory Data Analysis (EDA): Jupyter Notebook for preliminary understanding, cleaning, and feature engineering to obtain performance indicators.

• Key Performance Analysis: Jupyter Notebook for in-depth analysis, such as statistical testing, to reveal future insights and confirm hypotheses.

• Comprehensive Reporting: An exhaustive PDF report of the findings, insights, and strategic suggestions.

• Interactive Dashboard: A Power BI dashboard for interactive visualization of data and easy exploration of vendor performance metrics.

• SQLite Database: Use of a light-weight, file-based database for effective data storage and querying.


🛠️ Technologies Used

• Python:

   o pandas: For data manipulation and analysis.
   
   o sqlite3 (standard library): For working with the SQLite database.
   
   o sqlalchemy: For creating and managing database engines.
   
   o matplotlib & seaborn: For data visualization in notebooks.
   
   o scipy.stats: For statistical analysis and hypothesis testing.
   
   o os, logging, time: For utility functions and logging.

• SQLite (.db files): The database system used to store all raw and processed data.

• Power BI Desktop: Used to develop the interactive dashboard and visual reports.

• Jupyter Notebook: Used for interactive data processing and analysis step documentation and development.

• CSV Files: Source of raw data.


Power BI Desktop: Download and install [Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494) if you haven't already. This is necessary to view and interact with the Vendor_Summary_Dashboard.pbix file.


Dataset Download: [Vendor Performance Analysis](https://www.kaggle.com/datasets/vivekkumarkamat/vendor-performance-analysis)


🚀 Usage

Read the steps below in sequence to operate the analysis and produce the insights:

1. Data Ingestion (ingestion.ipynb):

   o Open ingestion.ipynb in Jupyter Notebook.
   
   o Execute all cells. This notebook will handle reading the CSV files in the dataset/ directory and ingesting them into an SQLite database called inventory.db (which will be created in the root directory if it does not already exist).
   
   o A logs/ingestion_db.log file will be created in which the ingestion process will be tracked.

2. Exploratory Data Analysis (Exploratory_Data_Analysis.ipynb):
   
   o Run Exploratory_Data_Analysis.ipynb.
   
   o Run all cells. This notebook is connected to inventory.db, does some initial data cleaning, adds new calculated columns (e.g., GrossProfit, ProfitMargin, StockTurnover, SalesToPurchaseRatio), and creates a vendor_sales_summary table in the database for subsequent analysis.
   
   o Inspect the output cells for some preliminary insights into the dataset.

3. Vendor Performance Analysis (Vendor_Performance_Analysis.ipynb):

   o Open Vendor_Performance_Analysis.ipynb.
   
   o Execute all cells. This notebook does more advanced statistical analysis, such as hypothesis testing (e.g., comparing profit margins of top-performing vs. low-performing vendors using T-tests). It summarizes key insights that are essential for strategic decision-making.

4. Have a look at the Analysis Report (Vendor_Performance_Analysis_Report.pdf):

   o Load the Vendor_Performance_Analysis_Report.pdf file to see a pre-made, detailed summary of project results, statistical verification, and ultimate recommendations.

5. Investigate the Dashboard (Vendor_Summary_Dashboard.pbix):

   o Launch the Vendor_Summary_Dashboard.pbix file in Power BI Desktop.
   
   o Note: You might need to update the data source connection in Power BI to reference your local inventory.db file. Open File > Options and settings > Data source settings, choose the source, click Change Source., and navigate to your inventory.db file. Finally, click Refresh on the Home tab.
   
   o Explore the dashboard interactively to view vendor performance metrics, trends, and key findings visually.


💡 Insights and Recommendations

This project will assist in revealing key insights like:

• Top-performing and underperforming vendors by sales, profitability, and other important metrics.

• Product price optimization opportunities through comparison of profit margins.

• Inventory turnover and its effect on overall efficiency.
