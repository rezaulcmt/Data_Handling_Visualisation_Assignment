# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 01:53:12 2024

@author: Md Rezaul Karim
Student ID: 22094702
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the CSV file "world_development_data.csv" using pandas
data = pd.read_csv("world_development_data.csv")

# Define a list of specific countries of interest
specific_countries = (['India', 'Bangladesh', 'Nepal',
                      'Pakistan', 'Malaysia', 'Singapore'])

# Select only the rows from the dataframe where the 'Country' column matches the specified countries
data_select = data[data['Country'].isin(specific_countries)]

# Generate a summary of descriptive statistics for the selected data
data_summary = data_select.describe()


# Title and information
title = "World Development (1973-2022)"
name = "Name: Md Rezaul Karim"
student_id = "Student ID: 22094702"

# Overall message and descriptions for each plot
insight = "* Analyzing Economic and Population Trends"
plot1_explanation = " Plot-1: India is Top position in Mean GDP which is 1.5 according to chart"
plot2_explanation = " Plot-2: Singapore population grew the most from 2005 to 2010, but by 2021, it started to decrease. "
plot3_explanation = " Plot-3: In 2021 china population total was much than others country which is 38.6%"
plot4_explanation = " Plot-4: Singapore GDP groth is upeer quartile where as Banglaseh GDP groth is lower"

# Create a figure
plt.figure(figsize=(18, 10))

# Set the main title and background color
plt.suptitle(title, fontsize=24, fontweight='bold', color='Blue')
plt.gcf().set_facecolor('#87CEEB')

# Plot 1
plt.subplot(2, 2, 1)
sns.barplot(x='Country', y='GDP', data=data_select)
plt.title('Mean GDP for Specific Countries',
          fontsize=18, fontweight='bold', color='Green')
plt.xlabel('Country')
plt.ylabel('Mean GDP')

# Plot 2
plt.subplot(2, 2, 2)
sns.lineplot(x='Year', y='PopGrowth%', hue='Country',
             data=data_select, linewidth=2.5)
plt.title('Population Growth Over the Years for some Countries',
          fontsize=18, fontweight='bold', color='Green')
plt.xlabel('Year')
plt.ylabel('Population Growth (%)')
plt.grid(True, color='lightgray')  # Add Grid

# Plot 3
selected_year = 2021
data_selected_year = data[data['Year'] == selected_year]
top_countries = data_selected_year.nlargest(5, 'PopTotal')

plt.subplot(2, 2, 3)
plt.pie(top_countries['PopTotal'],
        labels=top_countries['Country'], autopct='%1.1f%%', startangle=90)
legend_labels = top_countries['Country'].tolist()
plt.legend(legend_labels, title='Countries', loc='upper left', bbox_to_anchor=(1, 0.6),
           fontsize='12', title_fontsize='14', labelspacing=0.8)
plt.title(f'Distribution of Population in {selected_year} (Top 5 Countries)',
          fontsize=18, fontweight='bold', color='Green')

# Plot 4
plt.subplot(2, 2, 4)
sns.boxplot(x='Country', y='GDPGrowth%', data=data_select)
plt.title('GDP Growth for some Countries',
          fontsize=18, fontweight='bold', color='Green')
plt.xlabel('Country')
plt.ylabel('GDP')

# Add text explanations
plt.figtext(0.5, 0.93, f"{name}, {student_id}",
            ha='center', va='center', fontsize=16)
plt.figtext(0.1, 0.12, insight, ha='left', va='center',
            fontsize=14, fontweight='bold', color='Magenta')
plt.figtext(0.1, 0.08, plot1_explanation, ha='left', va='center',
            fontsize=14, fontweight='bold', color='Magenta')
plt.figtext(0.1, 0.06, plot2_explanation, ha='left', va='center',
            fontsize=14, fontweight='bold', color='Magenta')
plt.figtext(0.1, 0.04, plot3_explanation, ha='left', va='center',
            fontsize=14, fontweight='bold', color='Magenta')
plt.figtext(0.1, 0.02, plot4_explanation, ha='left', va='center',
            fontsize=14, fontweight='bold', color='Magenta')

# Save the infographic
plt.savefig("22094702.png", dpi=300)
plt.show()
