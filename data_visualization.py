import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text

# Database setup
DATABASE_URL = 'postgresql+psycopg2://postgres:new_password@localhost/machine_data'
engine = create_engine(DATABASE_URL)

# Queries to fetch data
query = text('SELECT * FROM public.machine_inputs')
df = pd.read_sql(query, engine)

# Ensure 'timestamp' is a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 12))  # Increase figure height

# Adjust spacing between plots
plt.subplots_adjust(hspace=0.6, wspace=0.4)  # Increase hspace

# Plot 1: Line plot for temperature over time
sns.lineplot(data=df[df['sensor_type'] == 'temperature'], x='timestamp', y='value', ax=axs[0, 0], color='blue', linewidth=2, label='Temperature', linestyle='-')
axs[0, 0].set_title('Temperature Over Time')
axs[0, 0].set_xlabel('Timestamp')
axs[0, 0].set_ylabel('Temperature')
axs[0, 0].legend()
axs[0, 0].tick_params(axis='x', rotation=45)
axs[0, 0].lines[0].set_linewidth(3)  # Thicker line
axs[0, 0].lines[0].set_alpha(0.8)    # Adjust transparency

# Plot 2: Line plot for humidity over time
sns.lineplot(data=df[df['sensor_type'] == 'humidity'], x='timestamp', y='value', ax=axs[0, 1], color='green', linewidth=2, label='Humidity', linestyle='-')
axs[0, 1].set_title('Humidity Over Time')
axs[0, 1].set_xlabel('Timestamp')
axs[0, 1].set_ylabel('Humidity')
axs[0, 1].legend()
axs[0, 1].tick_params(axis='x', rotation=45)
axs[0, 1].lines[0].set_linewidth(3)  # Thicker line
axs[0, 1].lines[0].set_alpha(0.8)    # Adjust transparency

# Plot 3: Histogram of sensor values
sns.histplot(df['value'], bins=30, ax=axs[1, 0], color='purple')
axs[1, 0].set_title('Histogram of Sensor Values')
axs[1, 0].set_xlabel('Value')
axs[1, 0].set_ylabel('Frequency')

# Plot 4: Box plot of sensor values by type
sns.boxplot(data=df, x='sensor_type', y='value', ax=axs[1, 1], palette='pastel')
axs[1, 1].set_title('Box Plot of Sensor Values by Type')
axs[1, 1].set_xlabel('Sensor Type')
axs[1, 1].set_ylabel('Value')

# Show the plot
plt.show()
