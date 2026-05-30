# Architecture Overview

## Purpose

This document summarizes the architecture of the Ministry MEL/MIS Ecosystem Simulation. The solution demonstrates how raw ministry reporting data can be transformed into a structured enterprise analytics platform using DuckDB, SQL/dbt-style transformations, dimensional modeling, and Power BI.

## High-Level Architecture

Raw Ministry Reports

↓

DuckDB Analytical Database

↓

SQL/dbt Transformation Layer

↓

Power BI Semantic Model

↓

Dashboards and Analytical Reports

↓

Executives, Program Managers, Analysts, and Provincial Users

## Data Flow

1. Raw reporting data is generated for MCTI and MGEE.
2. Data is loaded into DuckDB.
3. SQL/dbt-style models transform raw records into reporting-ready views.
4. Power BI connects to DuckDB through ODBC.
5. Power BI semantic modeling organizes dimensions, facts, measures, and relationships.
6. Dashboards provide executive, operational, data quality, time intelligence, geospatial, and drillthrough analytics.

## Semantic Model

The Power BI semantic model uses conformed dimensions connected to multiple fact-style tables.

### Conformed Dimensions

- dim_date
- dim_ministry
- dim_province

### Fact / Reporting Tables

- pbi_ministry_performance
- pbi_dq_scorecard
- pbi_dq_exceptions

## Relationship Design

Each conformed dimension filters the fact tables using one-to-many relationships.

Examples:

- dim_ministry filters ministry performance, DQ scorecard, and DQ exceptions.
- dim_province filters province-level reporting, maps, DQ dashboards, and RLS.
- dim_date supports time intelligence across performance and DQ reporting.

## Key Architecture Principles

### Conformed Dimensions

Shared dimensions ensure consistent filtering, slicing, drillthrough, and security across all reporting tables.

### Star Schema Design

The model follows a Kimball-style star schema approach where dimensions filter facts.

### Centralized Measures

Measures are organized in a dedicated measures table to support reuse and consistent calculations.

### Data Quality Layer

Data quality logic is modeled upstream using SQL/dbt-style views instead of relying on complex visual-level filters.

### Security Layer

Row Level Security is implemented through dim_province, allowing province-based access control.

## Enterprise Features Demonstrated

- Dimensional modeling
- Date dimension and date_key
- Data quality exception modeling
- Azure Maps geospatial reporting
- Drillthrough analysis
- Row Level Security
- Time intelligence
- Reusable semantic measures

## Architecture Value

The architecture demonstrates how a ministry reporting environment can evolve from raw submissions into a governed analytics platform suitable for executive oversight and operational decision-making.
