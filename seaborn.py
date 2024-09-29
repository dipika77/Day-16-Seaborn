#Data visualization with Seaborn

#instructions
'''Import Matplotlib and Seaborn using the standard naming convention.
Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
Display the plot.
'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()


#instructions
'''Import Matplotlib and Seaborn using the standard naming conventions.
Use Seaborn to create a count plot with region on the y-axis.
Display the plot.'''

# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt


# Create count plot with region on the y-axis
sns.countplot(y= region)

# Show plot
plt.show()


#using pandas with seaborn

#instructions
'''Read the csv file located at csv_filepath into a DataFrame named df.
Print the head of df to show the first five rows.'''

# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())



#instructions
'''mport Matplotlib, pandas, and Seaborn using the standard names.
Create a DataFrame named df from the csv file located at csv_filepath.
Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
Display the plot.'''

# Import Matplotlib, pandas, and Seaborn
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot( x = 'Spiders', data = df)

# Display the plot
plt.show()


#Adding a third variable with hue

#instructions
'''Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. Color the plot points based on "location" (urban vs. rural).
Make "Rural" appear before "Urban" in the plot legend.'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location")

# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()


#  instructions
'''Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
Create a count plot with "school" on the x-axis using the student_data DataFrame.
Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot( x = 'school', data = student_data, hue ='location',  palette=palette_colors)

# Display plot
plt.show()


#Introduction to relational plots and subplots

#instructions
'''Modify the code to use relplot() instead of scatterplot().
Modify the code to create one scatter plot for each level of the variable "study_time", arranged in columns.
Adapt your code to create one scatter plot for each level of a student's weekly study time, this time arranged in rows.'''

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter")

# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            col="study_time")

# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()




#instructions
'''Use relplot() to create a scatter plot with "G1" on the x-axis and "G3" on the y-axis, using the student_data DataFrame.
Create column subplots based on whether the student received support from the school ("schoolsup"), ordered so that "yes" comes before "no".
Add row subplots based on whether the student received support from the family ("famsup"), ordered so that "yes" comes before "no". This will result in subplots based on two factors.'''

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row = 'famsup', row_order = ['yes', 'no'])

# Show plot
plt.show()


#Customizing scatter plots
#instructions
'''Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders in the car ("cylinders").
To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders", hue = 'cylinders')

# Show plot
plt.show()


#instructions
'''Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on the y-axis. Vary the style and color of the plot points by country of origin ("origin").'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x = 'acceleration', y = 'mpg', data = mpg, kind = 'scatter', style = 'origin', hue = 'origin')

# Show plot
plt.show()


#introduction to line plots
#instructions

'''Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.'''

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot( x = 'model_year', y = 'mpg', data = mpg, kind = 'line')

# Show plot
plt.show()


#instructions
'''Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean'''

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci = 'sd')

# Show plot
plt.show()


#instructions
'''Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis. Turn off the confidence intervals on the plot.
Create different lines for each country of origin ("origin") that vary in both line style and color.
Add markers for each data point to the lines.
Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for each line.'''


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", markers = True, dashes = False)

# Show plot
plt.show()