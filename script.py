# Import the pandas library
import pandas as pd
# Import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Create a dictionary containing our data with dates
# Generate dates from January 10th to March 10th
start_date = datetime(2024, 1, 10)
end_date = datetime(2024, 3, 10)
# Calculate days between
days_between = (end_date - start_date).days
# Create 6 evenly spaced dates for our data points
dates = [start_date + timedelta(days=i*days_between/5) for i in range(6)]
date_strings = [date.strftime('%Y-%m-%d') for date in dates]

data = {
    "Date": date_strings,
    "Number of Mr. Flower's face in the classroom": [0, 2, 3, 4, 6, 7],
    "Number of times Caidan has shown up": [1, 3, 4, 8, 10, 11]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Convert date strings back to datetime for plotting
df['Date'] = pd.to_datetime(df['Date'])

# Create a line plot
plt.figure(figsize=(12, 6))

# Plot both data series
plt.plot(df['Date'], df["Number of Mr. Flower's face in the classroom"], 
         marker='o', linestyle='-', color='blue', label="Mr. Flower's face")
plt.plot(df['Date'], df["Number of times Caidan has shown up"], 
         marker='s', linestyle='-', color='green', label="Caidan showing up")

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Count')
plt.title("Pictures of Mr. Flower's Face and Caidan Showing Up Over Time")

# Format x-axis to show dates nicely
plt.gcf().autofmt_xdate()

# Add legend
plt.legend()

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Ensure the layout looks good
plt.tight_layout()

# Show the plot
plt.show()
