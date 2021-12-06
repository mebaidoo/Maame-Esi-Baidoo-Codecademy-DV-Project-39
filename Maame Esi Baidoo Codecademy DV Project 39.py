#Importing the modules that will be used
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
#Loading the world cup csv file into a pandas dataframe
df = pd.read_csv("WorldCupMatches.csv")
#Inspecting the dataframe
print(df.head())
#Adding a new column containing the total goals scored
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]
print(df.head())
#Creating a bar chart visualizing how many goals were scored each year
#Setting the style of the plot to be whitegrid
sns.set_style("whitegrid")
#Setting the context to be poster to make the text in the visualization bigger and easier to read and adjusting the font size
sns.set_context("poster", font_scale = 0.8)
#Creating a figure and axes for the plot
f, ax = plt.subplots(figsize = (12, 7))
ax = sns.barplot(df["Year"], df["Total Goals"])
#Giving the bar chart a title
ax.set_title("Average Number of Goals Scored Yearly")
plt.show()
plt.clf()
#creating a box plot to visualize the distribution of the goals data
#Loading the goals csv data into a dataframe
df_goals = pd.read_csv("goals.csv")
print(df_goals.head())
#Setting the context of the next plot to be notebook and the font size to be 1.25
sns.set_context("notebook", font_scale = 1.25)
#Creating aa figure for the next plot
f, ax2 = plt.subplots(figsize = (12, 7))
#Drawing the box plot
ax2 = sns.boxplot(x = "year", y = "goals", data = df_goals, palette = "Spectral")
ax2.set_title("Distribution of goals between 1930 and 2014")
plt.show()
#Visualizing the distribution of the number of goals using a KDE plot
plt.clf()
sns.kdeplot(data = df_goals["goals"], shade = False)
plt.show()