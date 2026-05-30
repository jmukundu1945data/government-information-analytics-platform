# DAI Ministry MEL/MIS Ecosystem Simulation

## Project Overview

This project is a realistic simulation of a Ministry Monitoring, Evaluation, Learning and Management Information System (MEL/MIS) designed to demonstrate enterprise analytics engineering, dimensional modeling, semantic data modeling, data quality management, executive reporting, geospatial analytics, drillthrough analysis, and row-level security.

The solution simulates reporting operations for two ministries:

- Ministry of Commerce, Trade and Industry (MCTI)
- Ministry of Green Economy and Environment (MGEE)

Rather than focusing only on dashboard development, the project emphasizes the complete analytical lifecycle from data modeling through decision support.

## Architecture Snapshot

![Solution Architecture](architecture/solution_architecture.png)

---

## Why This Project Was Built

Many reporting systems focus heavily on collecting data but provide limited analytical capability.

The purpose of this simulation was to demonstrate how modern analytics engineering principles can transform ministry reporting data into an enterprise decision-support platform capable of serving:

- Executives
- Program Managers
- M&E Officers
- Data Managers
- Analysts
- Provincial Users

---

## Solution Architecture

The solution follows a modern analytics engineering architecture:

### Data Layer

DuckDB was used as the analytical database layer.

Responsibilities:

- Data storage
- Analytical querying
- Business reporting views

### Transformation Layer

SQL and dbt-style modeling principles were used to create reporting-ready structures.

Examples:

- Ministry performance views
- Data quality scorecards
- Data quality exception reporting

### Semantic Layer

Power BI was used as the semantic model and reporting layer.

The semantic model is built around conformed dimensions:

- dim_date
- dim_ministry
- dim_province

and reporting tables:

- pbi_ministry_performance
- pbi_dq_scorecard
- pbi_dq_exceptions

---

## Enterprise Features Demonstrated

### Dimensional Modeling

Implemented a Kimball-style dimensional model using:

- Conformed dimensions
- Star schema principles
- Shared business entities

### Semantic Modeling

Implemented:

- Reusable DAX measures
- Centralized business calculations
- Consistent filtering behavior

### Time Intelligence

Implemented:

- Date Dimension
- date_key
- Year-to-Date (YTD) analysis
- Month-over-Month (MoM) analysis
- Trend reporting

### Data Quality Monitoring

Implemented:

- Data Quality Scorecards
- Missing Value Monitoring
- Negative Value Detection
- Data Quality Exception Reporting

### Geospatial Analytics

Implemented:

- Azure Maps
- Province-level reporting
- Geographic performance visualization

### Drillthrough Analytics

Implemented:

- Province-to-District investigation
- Indicator-level exploration
- Context-aware navigation

### Row Level Security (RLS)

Implemented:

- Province-specific security roles
- Conformed dimension-based filtering
- Enterprise-style access control

---

## Dashboard Portfolio

### Executive Overview

High-level KPI monitoring and executive visibility.

![Executive Overview dashboard](screenshots/01_Executive_Overview.png)

### Ministry Performance Analysis

Performance analysis by ministry, indicator, and province.

![Ministry Performance dashboard](screenshots/02_Ministry_Performance.png)

### Data Quality Dashboard

Monitoring of reporting quality and exception management.

![Data Quality dashboard](screenshots/03_Data_Quality.png)

### Provincial Reporting Dashboard

Province and district performance analysis.

### Indicator Analysis Dashboard

Indicator-level reporting and performance review.

### Trend & Time Intelligence Dashboard

YTD, MoM, and trend monitoring.

![Time Intelligence dashboard](screenshots/04_Time_Intelligence.png)

### Geospatial Performance Dashboard

Azure Maps-based geographic reporting.

![Geospatial Performance dashboard](screenshots/05_Geospatial_Map.png)

### Province Drillthrough Dashboard

Analyst-oriented investigative reporting.

### Row-Level Security Demo

Province-specific reporting access demonstration.

![Row-Level Security demo](screenshots/06_RLS_Demo.png)

---

## Key Analytics Engineering Lessons

The most important lessons from this project were:

### Conformed Dimensions Simplify Everything

The dimensions:

- Province
- Ministry
- Date

became the foundation for:

- Security
- Drillthrough
- Time Intelligence
- Geographic Analysis
- Dashboard Interactivity

### Good Modeling Enables Advanced Features

Features such as:

- RLS
- Drillthrough
- Azure Maps
- Time Intelligence

became significantly easier because the underlying model was designed correctly.

### Data Quality Should Be Built Into The Architecture

Data quality monitoring should not be treated as an afterthought.

The project demonstrated how DQ scorecards and exception reporting can become first-class analytical products.

### Human Oversight Remains Essential

AI tools accelerated development significantly, but critical improvements came from:

- Business realism validation
- Dimensional modeling decisions
- Semantic design
- Relationship management
- Time intelligence design

---

## Technology Stack

### Data Platform

- DuckDB

### Analytics Engineering

- SQL
- dbt-style modeling concepts

### Business Intelligence

- Power BI
- DAX
- Azure Maps

### AI-Assisted Development

- ChatGPT
- Codex
- Continue

---

## How to Reproduce / Run Locally

This repository includes the simulated DuckDB database, dbt-style transformation project, ingestion scripts, Power BI model, architecture diagram, and dashboard screenshots needed to review the solution.

### Prerequisites

- Python 3.10+
- DuckDB Python package
- dbt with the DuckDB adapter
- Power BI Desktop

### Rebuild the Analytical Data Layer

From the repository root:

```powershell
python ingestion\scripts\load_ministry_reports.py
```

This loads the simulated ministry reporting CSV files into:

```text
database/ministry_mis.duckdb
```

### Run the dbt Models

The dbt project lives in:

```text
dbt_ministry_mis/ministry_mis/
```

Create or update your local dbt profile named `ministry_mis` so it points to the DuckDB database:

```yaml
ministry_mis:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: ../../database/ministry_mis.duckdb
```

Then run:

```powershell
cd dbt_ministry_mis\ministry_mis
dbt parse
dbt build
```

The dbt models create staging, conformed dimensions, analytical marts, data quality views, and Power BI-ready reporting views.

### Review the Power BI Report

Open the Power BI report file:

```text
dbt_ministry_mis/ministry_mis/models/powerbi/pbix/mcti_mgee_sim.pbix
```

The dashboard screenshots in the `screenshots/` folder show the main report pages for quick GitHub review.

---

## Repository Structure

```text
DAI_MIS_SIMULATION/
|-- architecture/
|-- consultancy_outputs/
|-- database/
|-- dbt_ministry_mis/
|-- Docs/
|-- ingestion/
|-- screenshots/
|-- shared_reference/
|-- simulation_scripts/
`-- README.md
```

---

## Documentation

See the Docs folder for:

- Executive Summary
- Architecture Overview
- Dashboard Catalog
- Lessons Learned

---

## Final Reflection

This project demonstrates that enterprise analytics solutions are not primarily about dashboards.

They are about:

- Data Modeling
- Semantics
- Architecture
- Governance
- Security
- Business Understanding

The simulation was intentionally designed to showcase analytics engineering thinking and enterprise reporting concepts rather than simply producing visualizations.

---

## Author

Jonathan Mukundu

Analytics Engineering Portfolio Project

Focus Areas:

- Analytics Engineering
- Power BI
- Data Quality
- Government MIS Systems
- Semantic Modeling
- Decision Support Systems
- Geospatial Reporting
