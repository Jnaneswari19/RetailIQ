# 📊 RetailIQ - Sales Management & Analytics Dashboard

## 🚀 Transform Retail Data into Actionable Business Insights

RetailIQ is an end-to-end Sales Management and Business Analytics Dashboard that enables businesses to manage customers, products, and sales while gaining real-time insights through interactive visualizations and downloadable reports.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

RetailIQ is a Python-based Sales Management and Analytics System that helps businesses manage customers, products, and sales while providing interactive business insights through a Streamlit dashboard.

The project integrates MySQL for database management, Pandas for data analysis, SQLAlchemy for database connectivity, and Streamlit for creating a modern web dashboard.

---
## ⭐ Project Highlights

- End-to-End Retail Sales Management System
- Interactive Streamlit Dashboard
- MySQL Relational Database
- SQLAlchemy Database Integration
- Secure Admin Authentication
- Business KPI Dashboard
- Interactive Charts & Visual Analytics
- CSV, Excel & PDF Report Export
- Logging and Error Handling

# Features

## Customer Management
- Add customer records
- View customer information
- Manage customer database

## Product Management
- Add products
- Store product details
- Maintain product catalog

## Sales Management
- Record sales transactions
- Track customer purchases
- Store sales history

## Dashboard
- Secure Admin Login
- Interactive Sidebar Filters
- KPI Cards
- Sales Data Table
- Monthly Revenue Analysis
- Customer Revenue Analysis
- Product Performance Analysis

## Data Visualization
- Monthly Revenue Bar Chart
- Sales Trend Line Chart
- Revenue Area Chart
- Product Revenue Pie Chart
- Customer Revenue Donut Chart

## Report Generation
- CSV Export
- Excel Export (.xlsx)
- PDF Export

## Logging
- Application Logs
- Database Logs
- Error Logs
- Report Generation Logs

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| MySQL | Database |
| SQLAlchemy | Database Connectivity |
| Pandas | Data Analysis |
| Streamlit | Dashboard |
| Matplotlib | Charts |
| OpenPyXL | Excel Export |
| FPDF2 | PDF Export |
| PyMySQL | MySQL Driver |

---

# Project Structure

```
RetailIQ/
│
├── analytics/
│   ├── reports.py
│   └── sales_analysis.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── sample_data.py
│
├── database/
│   ├── database.py
│   ├── schema.sql
│   └── insert_data.sql
│
├── docs/
│   └── project_notes.md
│
├── modules/
│   ├── customer.py
│   ├── product.py
│   └── sales.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── main.py
├── check_data.py
└── .gitignore
    LICENSE
```

---

# Database Schema

The system uses three relational tables:

- Customers
- Products
- Sales

Relationships

```
Customers
    │
    │ customer_id
    │
Sales
    │
    │ product_id
    │
Products
```

---

# Installation

## 1 Clone the Repository

```bash
git clone https://github.com/Jnaneswari19/RetailIQ.git
```

---

## 2 Open Project

```bash
cd RetailIQ
```

---

## 3 Create Virtual Environment

```bash
python -m venv venv
```

---

## 4 Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6 Create Database

Open MySQL and execute

```sql
source database/schema.sql;
source database/insert_data.sql;
```

---

## 7 Update Database Credentials

Modify the MySQL username and password in

```
dashboard/app.py
```

Example

```python
engine = create_engine(
    "mysql+pymysql://root:password@localhost:3306/retailiq"
)
```

---

## 8 Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Dashboard Features

The dashboard includes:

- Secure Login
- Sidebar Filters
- KPI Cards
- Monthly Revenue
- Top Customers
- Top Products
- Interactive Charts
- Sales Data Table
- CSV Download
- Excel Download
- PDF Download

---

# Reports Generated

- Monthly Sales Report
- Top Customers Report
- Top Products Report
- Revenue Summary
- Excel Report
- PDF Report

---


# Screenshots

## Login Page

![Login Page](Screenshots/login_page.png)

---

## Dashboard Home

![Dashboard Home](Screenshots/dashboard_home.png)

---

## Sidebar Filters

![Sidebar Filters](Screenshots/filters_sidebar.png)

---

## KPI Cards

![KPI Cards](Screenshots/kpi_cards.png)

---

## Monthly Revenue Chart

![Monthly Revenue](Screenshots/monthly_revenue_chart.png)

---

## Product Revenue Distribution

![Pie Chart](Screenshots/product_revenue_pie_chart.png)

---

## Customer Revenue Distribution

![Donut Chart](Screenshots/customer_revenue_donut_chart.png)

---

## Sales Data Table

![Sales Table](Screenshots/sales_data_table.png)

---

## Export Reports

![Export Reports](Screenshots/export_reports.png)

---

# Future Improvements

- Inventory Management
- Supplier Module
- Customer Authentication
- Role-Based Access
- Machine Learning Sales Forecasting
- Email Report Scheduling
- Cloud Deployment
- REST API Integration

---
## 👩‍💻 Author

**Jnaneswari**

Python Developer | Data Analytics Enthusiast

GitHub:
https://github.com/Jnaneswari19

---
# 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

This project was developed as a hands-on learning project to strengthen skills in Python, SQL, Data Analysis, Database Management, and Dashboard Development.