# Composite Economic Performance Index for Southeast Asian and Pacific Countries

## Overview

This project constructs a **Composite Economic Performance Index (CEPI)** for Southeast Asian and selected Pacific countries. The aim is to provide a comprehensive comparison of economic performance by combining multiple macroeconomic and development indicators.

## Theoretical Framework

The theoretical basis for this index assumes that economic performance is a multifactorial construct, influenced not only by GDP but also by other macroeconomic, social, and infrastructural indicators. These dimensions together provide a holistic view of a nation's development and economic stability.

## Methodology

### Data Collection

The project includes a wide range of indicators that are believed to reflect different facets of a country’s economic performance and development level:

- **Macroeconomic Indicators**:
  - GDP per capita (PPP)
  - GDP growth rate
  - Final consumption expenditure
  - Government debt
  - Inflation annually
  - Current account balance
  - Exports of goods and services
  - Imports of goods and services

- **Labor and Demographics**:
  - Labour force participation rate
  - Unemployment rate
  - Life expectancy at birth
  - School enrollment

- **Infrastructure and Technology**:
  - Access to electricity
  - Access to internet
  - Mobile cellular subscriptions

- **Governance and Logistics**:
  - LPI (Logistics Performance Index) Score
  - CPI (Corruption Perceptions Index)
  - Political Stability and Absence of Violence/Terrorism Percentile Rank
  - Regulatory Quality dataset

- **Environmental Indicators**:
  - CO₂ Emissions
  - CO₂ Emissions per capita
  - Renewable energy consumption

### Data Preprocessing

- Standardization using `StandardScaler` to bring all indicators onto the same scale.
- Handling of missing values where necessary.
- Indicators are combined using statistical aggregation techniques.

### Index Construction

Each country's performance on these indicators is used to compute a composite score, allowing comparative analysis between nations.

### Visualization

Visual comparisons and statistical charts are generated using:
- `Matplotlib`
- `Seaborn`

## Tools and Libraries

- `pandas` for data manipulation
- `matplotlib` and `seaborn` for plotting
- `sklearn.preprocessing` for data normalization
- `statsmodels` for potential regression analysis

## Usage

1. Ensure all data files (CSV/Excel) are available in the project directory.
2. Open and run `main.ipynb` to:
   - Load and preprocess data
   - Calculate composite index
   - Generate comparative visualizations

## Results

The output includes country rankings and comparative visualizations that highlight economic strengths and weaknesses across multiple dimensions.

## Future Work

- Apply weighting methods like PCA or expert-informed weighting
- Introduce interactive dashboards
- Explore time-series trend analysis

---

> **Note**: The values for each indicator in the index are currently placeholders (`0`) and will be populated with real data from the corresponding datasets.

