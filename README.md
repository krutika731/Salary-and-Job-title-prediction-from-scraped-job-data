# Salary-and-Job-title-prediction-from-scraped-job-data

For this project I scraped job data from Seek and Indeed and scraped features like Job title, Location, Salary, Description, and Company.

To scrape data I used Scrapy framework and link for that file is given below.
[Indeed scarping file][https://github.com/krutika731/Salary-and-Job-title-prediction-from-scraped-job-data/blob/master/indeed_data.py]
[Seek scraping file][https://github.com/krutika731/Salary-and-Job-title-prediction-from-scraped-job-data/blob/master/seek_scrape.py]

To run that file go to command prompt and move to the path where you have saved that file
Now, write following command to start  scraping data from Seek and Indeed

- scrapy runspider indeed_data.py
- scrapy runspider seek_data.py

To save the scraped result in csv file for future use write following commands.

- scrapy runspider indeed_data.py -o indeed_data.csv
- scrapy runspider seek_data.py -o seek_data.csv


After scraping job data I cleaned the data like,
- Removed HTML tags from job description
- Impute the yearly salary from the given hourly, weekly and monthly salary

Link of the notebook to clean job data is given below.
[Data cleaning notebook][https://github.com/krutika731/Salary-and-Job-title-prediction-from-scraped-job-data/blob/master/data%20cleaning.ipynb]

After cleaning the main objective of the project is,
1. to predict the salary based on the given data
2. to predict the job title from the given job description

For the first part of the project, to predict Salary, the following steps are applied,
- Divided salary data into three class as High, Low and Medium salaries based on certain condition
- Upsample Low and Medium class data to balance classes
- Preprocessing text(job description and job titles) to remove punctuation marks, numerical data and converting data to lower case
- Used CountVectorizer and TfidfVectorizer to convert your textual data in numerical data based on the frequency of words.
- Include other features such as location along with job titles, and job description to improve the result
- Reduced dimension using TruncatedSVD to prevent the model from overfitting
- Applied different Classification algorithm to see the results of each algorithm
- Found the best algorithm for classification and tuned hyperparameters to improve the result.

The link for the above part is given in the below link.
[Part-1 notebook][https://github.com/krutika731/Salary-and-Job-title-prediction-from-scraped-job-data/blob/master/question-1_notebook.ipynb]

For the second part of the project, to predict Job titles, the following steps are applied,
- Preprocessed text of job description to remove punctuation marks, numerical data and converting text to lower case
- Used CountVectorizer and TfidfVectorizer to convert textual data into numerical data
- Reduced dimensions using TruncetedSVD to prevent the model from overfitting
- Applied different classification algorithm to see the results of each algorithm
- Found the best algorithm for classification and tuned hyperparameter to improve the result


The link for the above part is given in the below link.
[Part-2 notebook][https://github.com/krutika731/Salary-and-Job-title-prediction-from-scraped-job-data/blob/master/question-2_notebook.ipynb]
The code
