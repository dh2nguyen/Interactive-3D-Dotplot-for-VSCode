# Tissue Spatial Geometrics Lab (www.TSG-Lab.org)
# David H. Nguyen, PhD

###### Instructions ######
# 0. This script was written to be run in VSCode or an IDE that allows
#    interactive graphical pop-up windows.
# 1. The input file should be a CSV file that is formatted as seen below. 
# 2. The csv file MUST contain a column that has labels for each category. The name of this column
#    must be speclled as "Category".
#      -Example of Categories: Dog, Cat, CarType, FavoriteFood, etc.
#      -If you don't have any categories, then the rows in this column should have some word, 
#       like "NA". The rows of this column should not be empty.
# 3. Paste in the file path to the working directory in Step 1.
# 4. Paste in the name of the input file in Step 2. Then run the whole script. 
#
# The input file should be formatted like this: 
#  
#  Category   SampleName    PC1     PC2     PC3
#  Dog        Woofy         0.2     0.3     0.1
#  Dog        Spikey        0.3     0.2     0.8
#  Cat        Tinker        0.04    0.1     0.03
#  Cat        Whiskas       0.07    0.11    0.06
#
######

# Load the dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Step 1. Set the working directory
os.chdir("/Users/davidnguyen/Downloads/temp/")  # Paste in the file path to your working directory

# Step 2. Load the CSV file
file_path = "1st3PCvalues.csv" # paste in the name of your csv
df = pd.read_csv(file_path)

# Step 3 and On
# Extract PCA coordinates
x = df['PC1']
y = df['PC2']
z = df['PC3']

# Assume there's a column called 'Category'
categories = df['Category'].unique()
cmap = plt.get_cmap('viridis')
norm = mcolors.Normalize(vmin=0, vmax=len(categories) - 1)
category_to_color = {cat: cmap(norm(i)) for i, cat in enumerate(categories)}

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points by category
for category in categories:
    idx = df['Category'] == category
    ax.scatter(x[idx], y[idx], z[idx],
               color=category_to_color[category],
               label=category, s=50, edgecolors='k')

# Add labels and title
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.set_title("3D PCA Plot with Category Legend")

# Add legend
ax.legend(title="Categories")

# Show plot
plt.show()
