import pandas as pd

# Define standard missing value markers
missing_values = ["..", "...", "no data", "", "N/A", "#VALUE!", "na"]

# ---- Macroeconomic Indicators ----
df_gdp_per_capita = pd.read_csv('GDP per capita (PPP).csv', na_values=missing_values)
df_gdp_growth_rate = pd.read_csv('GDP growth rate.csv', na_values=missing_values)
df_FCE = pd.read_csv('Final consumption expenditure.csv', na_values=missing_values)
df_gov_debt = pd.read_excel('Government debt.xls', na_values=missing_values)
df_inflation = pd.read_csv('Inflation annually.csv', na_values=missing_values)

# ---- Human Capital ----
df_labour_force = pd.read_csv('Labour Force Participant Rate.csv', na_values=missing_values)
df_life_expectancy_at_birth = pd.read_csv('Life expectancy at birth.csv', na_values=missing_values)
df_school_enrollment = pd.read_csv('School enrollment.csv', na_values=missing_values)
df_unemployment_rate = pd.read_excel('Unemployment rate.xls', na_values=missing_values)

# ---- Infrastructure and Technology ----
df_access_to_electricity = pd.read_csv('Access to electricity.csv', na_values=missing_values)
df_access_to_internet = pd.read_csv('indivisual using the internet.csv', na_values=missing_values)
df_mobile_subscriptions = pd.read_csv('Mobile cellular subscriptions.csv', na_values=missing_values)
df_LPI_Score = pd.read_excel('LPI Score.xlsx', na_values=missing_values)

# ---- Institutions and Political Factors ----
df_CPI = pd.read_excel("CPI2023_Global_Results__Trends.xlsx", skiprows=3, engine='openpyxl', na_values=missing_values)
df_political_stability = pd.read_csv("Political Stability and Absence of ViolenceTerrorism Percentile Rank.csv", na_values=missing_values)

# ---- WGI Dataset ----
df_wgi_data_set = pd.read_excel("wgidataset.xlsx", na_values=missing_values)

# ---- Trade and Environmental Factors ----
df_current_account_balance = pd.read_csv("current accoung balance (Macroeconomic Indicators ).csv", na_values=missing_values)
df_exports = pd.read_csv("Exports of goods and services.csv", na_values=missing_values)
df_imports = pd.read_csv("Imports of goods and services.csv", na_values=missing_values)

# ---- Environment and Sustainability ----
df_CO2_emissions = pd.read_csv("CO2 Emission.csv", na_values=missing_values)
df_CO2_emissions_per_capita = pd.read_csv("CO2 Emission per capita.csv", na_values=missing_values)
df_renewable_energy_consumption = pd.read_csv("Renewable energy consumption.csv", na_values=missing_values)

# ---- Organize all for batch processing ----
dataframes = [
    df_gdp_growth_rate, df_gdp_per_capita, df_FCE, df_gov_debt, df_inflation,
    df_current_account_balance, df_exports, df_imports, df_labour_force,
    df_life_expectancy_at_birth, df_school_enrollment, df_unemployment_rate,
    df_access_to_electricity, df_access_to_internet, df_mobile_subscriptions,
    df_LPI_Score, df_CPI, df_political_stability, df_wgi_data_set,
    df_CO2_emissions, df_CO2_emissions_per_capita, df_renewable_energy_consumption
]

# Print sum of all missing valeues
def check_missing_values():
  print("The number of missing values in each dataset:")
  print("GDP per capita (PPP):", df_gdp_per_capita.isnull().sum().sum())
  print("GDP growth rate:", df_gdp_growth_rate.isnull().sum().sum())
  print("Final consumption expenditure:", df_FCE.isnull().sum().sum())
  print("Government debt:", df_gov_debt.isnull().sum().sum())
  print("Inflation annually:", df_inflation.isnull().sum().sum())
  print("Current account balance:", df_current_account_balance.isnull().sum().sum())
  print("Exports of goods and services:", df_exports.isnull().sum().sum())
  print("Imports of goods and services:", df_imports.isnull().sum().sum())
  print("Labour Force Participant Rate:", df_labour_force.isnull().sum().sum())
  print("Life expectancy at birth:", df_life_expectancy_at_birth.isnull().sum().sum())
  print("School enrollment:", df_school_enrollment.isnull().sum().sum())
  print("Unemployment rate:", df_unemployment_rate.isnull().sum().sum())
  print("Access to electricity:", df_access_to_electricity.isnull().sum().sum())
  print("Access to internet:", df_access_to_internet.isnull().sum().sum())
  print("Mobile cellular subscriptions:", df_mobile_subscriptions.isnull().sum().sum())
  print("LPI Score:", df_LPI_Score.isnull().sum().sum())
  print("CPI:", df_CPI.isnull().sum().sum())
  print("Political Stability and Absence of ViolenceTerrorism Percentile Rank:", df_political_stability.isnull().sum().sum())
  print("WGI dataset:", df_wgi_data_set.isnull().sum().sum())
  print("CO2 Emission:", df_CO2_emissions.isnull().sum().sum())
  print("CO2 Emission per capita:", df_CO2_emissions_per_capita.isnull().sum().sum())
  print("Renewable energy consumption:", df_renewable_energy_consumption.isnull().sum().sum())
  
check_missing_values()


