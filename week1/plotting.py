# Load and prepare data
import pandas as pd
import matplotlib.pyplot as plt

covid_data = pd.read_csv('swiss_covid_data_clean.csv')
grouped_data = covid_data.groupby('abbreviation_canton_and_fl')['current_isolated'].sum()

# Horizontal bar chart (best readability)

grouped_data.sort_values().plot(kind='barh', figsize=(10, 8))
plt.title('Isolated Cases by Canton')
plt.xlabel('Current Isolated Cases')
plt.tight_layout()
plt.show()