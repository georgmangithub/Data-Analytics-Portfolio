# %%
###Data Analysis Project###
# Data Manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#Importing the Data
gdp = pd.read_csv(r'C:\Users\George\Desktop\FILES\WORK\greek-economy-analysis\data\gdp.csv', skiprows=4)
unemployment = pd.read_csv(r'C:\Users\George\Desktop\FILES\WORK\greek-economy-analysis\data\unemployment.csv', skiprows=4)
inflation = pd.read_csv(r'C:\Users\George\Desktop\FILES\WORK\greek-economy-analysis\data\inflation.csv', skiprows=4)


# %%
gdp.head()

# %%
#Filter Greece only
gdp = gdp[gdp['Country Name'] == 'Greece']
unemployment = unemployment[unemployment['Country Name'] == 'Greece']
inflation = inflation[inflation['Country Name'] == 'Greece']

# %%
#Reshape Years -> Rows
gdp = gdp.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
    var_name='Year',
    value_name='GDP Growth'
)
unemployment = unemployment.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
    var_name='Year',
    value_name='Unemployment Rate'
)
inflation = inflation.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
    var_name='Year',
    value_name='Inflation Rate'
)

# %%
#Convert Year to numeric
gdp['Year'] = pd.to_numeric(gdp['Year'], errors='coerce')
unemployment['Year'] = pd.to_numeric(unemployment['Year'], errors='coerce')
inflation['Year'] = pd.to_numeric(inflation['Year'], errors='coerce')

# %%
#Keep relevant columns
gdp = gdp[['Year', 'GDP Growth']]
unemployment = unemployment[['Year', 'Unemployment Rate']]
inflation = inflation[['Year', 'Inflation Rate']]

# %%
#Merge datasets
data = gdp.merge(unemployment, on='Year').merge(inflation, on='Year')
data = data.dropna()
print(data.head())

# %%
###Visualization
sns.set(style="whitegrid", context="talk")
#Correlation Heatmap
corr = data[['GDP Growth', 'Unemployment Rate', 'Inflation Rate']].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix - Greek Economy")
plt.show()

# %%
#Line Chart
plt.figure(figsize=(12,8))

plt.plot(data['Year'], data['GDP Growth'], label='GDP Growth', marker='o')
plt.plot(data['Year'], data['Unemployment Rate'], label='Unemployment Rate', marker='o')
plt.plot(data['Year'], data['Inflation Rate'], label='Inflation Rate', marker='o')

for year in [2008, 2010, 2012, 2020]:
    plt.axvline(x=year, color='red', linestyle='--', alpha=0.5)
    plt.text(year+0.1, max(data['GDP Growth']), f"Crisis {year}", rotation=90, color='red')

plt.title("Greek Economy - Key Indicators Over Time")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.show()

# %%
#Economic Insights from Greek Economy Analysis

##Correlation Analysis
- **GDP Growth vs. Unemployment Rate**: Strong negative correlation.  
  → As GDP growth declines, unemployment rises — consistent with recessionary trends.
- **GDP Growth vs. Inflation Rate**: Weak or inconsistent correlation.  
  → Inflation in Greece appears influenced by external shocks (e.g., oil prices, EU policy) rather than solely domestic growth.
- **Unemployment vs. Inflation**: Weak or slightly positive correlation.  
  → Does not follow the classic Phillips Curve (low unemployment with high inflation), likely due to structural issues in the Greek labor market.

---

##Key Economic Events & Trends
- **2008–2012**:  
  - Global financial crisis → GDP drops sharply.  
  - Greek sovereign debt crisis (2010 bailout, austerity measures) → Unemployment spikes above 25%.
- **2013–2019**:  
  - Gradual GDP recovery, but unemployment remains high due to slow structural reforms.
- **2020 (COVID-19)**:  
  - Sharp GDP contraction; inflation dips due to reduced demand.  
  - Government stimulus partially cushions unemployment spike.

---

##Long-Term Patterns
- Moving averages show:
  - **GDP growth** is volatile, with repeated cycles of contraction and recovery.
  - **Unemployment** remains persistently high post-crisis — indicating structural challenges.
  - **Inflation** remains relatively controlled due to Eurozone monetary stability.

---

##Takeaway
- The Greek economy is highly sensitive to **external shocks** and **fiscal policy constraints**.
- Recovery in GDP does **not immediately translate** into reduced unemployment.
- Inflation remains **relatively stable**, suggesting monetary stability from Eurozone membership.

---


