Email Address Analysis System

Project Overview:
The Email Address Analysis System is a Python-based data processing application designed to validate, classify, analyze, and visualize email address data.
The system processes stored and user-input emails, extracts usernames and domains, categorizes domains into public and corporate types, performs statistical analysis, and generates structured reports with visual insights.

This project demonstrates practical implementation of:
File handling
Data validation
Dictionary-based grouping
Frequency analysis using Counter
Data visualization using Matplotlib
Persistent storage using CSV
Structured reporting

Key Features
Email Validation : 
Validates email structure and separates valid and invalid entries.

Username & Domain Extraction : 
Parses each email into:
Username
Domain name

Domain Classification : 
Classifies domains into:
Public (Gmail, Outlook, Yahoo)
Corporate (custom/business domains)

Analytics & Insights : 
Most common domain detection
Public vs corporate distribution
Top 5 domains ranking
Frequency-based analysis

Data Visualization : 
Generates:
Bar chart (Valid vs Invalid Emails)
Pie chart (Public vs Corporate Distribution)
Bar chart (Top 5 Domains)

Report Generation : 
Exports a structured CSV report including:
Domain
Category
Username
Summary statistics

Technologies Used : 
Python
CSV module
Collections (Counter)
Matplotlib
OS module
File handling

Learning Objectives : 
This project demonstrates understanding of:
Data structures (lists, dictionaries)
Data aggregation
Statistical counting
Visualization techniques
Persistent data storage
Software structuring fundamentals

How to Run : 
Clone the repository
Run the Python script
Enter email addresses when prompted
View generated visualizations
Check generated CSV report
