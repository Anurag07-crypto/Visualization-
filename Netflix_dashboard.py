import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Data loading

net=pd.read_csv("netflix_titles.csv",encoding="latin1")
l=['show_id', 'type', 'title', 'director', 'cast', 'country', 'release_year', 'rating', 'duration', 'listed_in', 'description']

# Data cleaning 


net.sort_values(by=["type","release_year"],ascending=[True,True],inplace=True)
net.fillna({"director":"Unknown"},inplace=True)
# net["cast"].fillna("Unknown",inplace=True) #old method 
net.fillna({"cast":"Unknown"},inplace=True)
net.fillna({"country":"Unknown"},inplace=True)
net.drop(columns="date_added",inplace=True)


# Visualization
def count_plot():
    sns.set_style("darkgrid")
    sns.countplot(x=net["release_year"].head(50),palette="gist_heat")
    plt.tight_layout()
    plt.show()
def histogram():
    sns.set_style("darkgrid")
    sns.histplot(net["release_year"],bins=15,palette="gist_heat",kde=True)
    plt.title("Content Over Time")
    plt.xlabel("Release_year")
    plt.ylabel("Content Overtime")
    plt.show()
# Top Content 
def top_10():
    print("Here are the top 10 country that produces more content\n")
    print(net["country"].value_counts().head(10))
def top_10_chart():
    top_countries = net["country"].value_counts().head(10)
    plt.pie(top_countries.values, labels=top_countries.index, autopct="%1.1f%%")
    plt.title("Top 10 country that produces more shows")
    plt.axis("equal")  # Keeps the pie chart round
    plt.tight_layout()
    plt.show()

# Main function
print("1.Content Over Time count plot")
print("2. Histogram of shows release over year")
print("3. Top 10 Country that produces more shows")
print("4. Top 10 Country that produces more shows Pie Chart\n")
print("<-----Enter your Choice if you want to exit then press 5 -------->")
while True:
    n=int(input("----> ")) 
    if n==1:
        count_plot()
    elif n==2:
        histogram()
    elif n==3:
        top_10()
    elif n==4:
        top_10_chart()
    elif n==5:
        print("Thanks for using ---------> 👋")
        break
    else:
        print("Thanks For using--------->")
        