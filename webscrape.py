# import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Fetches the data using requests
webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")


# Parses the content through Beautiful Soup
soup = BeautifulSoup(webpage.content, "html.parser")



#Uses Beautiful Soup to find all the HTML elements with a Rating class
returned_ratings = soup.find_all(attrs={"class": "Rating"})

ratings = []


#Appends the ratings returned to our ratings list
for rating in returned_ratings[1::]:
    ratings.append(float(rating.get_text()))



#Much like the method on line 19, this time uses the CSS selector to select all tags with the Company className
returned_companies = soup.select(".Company")

companies = []


#Appends companies from index 1 to our companies list
for company in returned_companies[1::]:
    companies.append(company.get_text())



cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")


#Does much the same as above, but removes the % symbol
for td in cocoa_percent_tags[1:]:
  percent = float(td.get_text().strip('%'))
  cocoa_percents.append(percent)



#Uses pandas to make a dataframe, showing all the companies, ratings and cocoa percentages
data = {"Companies": companies, "Ratings": ratings, "CocoaPercentage": cocoa_percents}
dataframe = pd.DataFrame.from_dict(data)



#groups the dataframe by companies and sorts them by average rating, then displays the ten largest
mean_values = dataframe.groupby("Companies").Ratings.mean()
ten_best = mean_values.nlargest(10)

print(ten_best)


