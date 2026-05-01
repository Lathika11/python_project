import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
data = pd.DataFrame({
    "Distance(km)": [2.5,5.0,1.2,7.8,3.5,10.0,4.2,6.5,2.0,8.3,1.8,3.0,9.5,4.8,6.0,2.3,7.2,3.8,5.5,1.5],
    "Delivery_Time(mins)": [15,30,10,45,20,60,25,40,12,50,11,18,55,28,35,14,42,22,33,9],
    "Vehicle_Type": ["Bike","Car","Bike","Car","Scooter","Car","Bike","Scooter","Bike","Car","Bike","Scooter","Car","Bike","Scooter","Bike","Car","Scooter","Car","Bike"],
    "Traffic_Level": ["Low","Medium","Low","High","Medium","High","Medium","High","Low","High","Low","Medium","High","Medium","High","Low","High","Medium","Medium","Low"],
    "Weather": ["Clear","Rainy","Clear","Foggy","Clear","Rainy","Clear","Foggy","Clear","Rainy","Clear","Clear","Foggy","Rainy","Clear","Clear","Foggy","Rainy","Clear","Clear"]
})

# Basic info
print(data.head())
print(data.describe())

# Visualization
sns.scatterplot(x="Distance(km)", y="Delivery_Time(mins)", hue="Vehicle_Type", data=data)
plt.title("Distance vs Delivery Time")
plt.show()

# Analysis
print("Average Delivery Time:", round(data["Delivery_Time(mins)"].mean(), 2))
print("Fastest Vehicle:", data.groupby("Vehicle_Type")["Delivery_Time(mins)"].mean().idxmin())
print("Highest Delay Traffic:", data.groupby("Traffic_Level")["Delivery_Time(mins)"].mean().idxmax())
