# import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


webpage = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")


soup = BeautifulSoup(webpage.content, "html.parser")


returned_ratings = soup.find_all(attrs={"class": "Rating"})

ratings = []

for rating in returned_ratings[1::]:
    ratings.append(float(rating.get_text()))



returned_companies = soup.select(".Company")

# print(returned_companies)
companies = []

for company in returned_companies[1::]:
    companies.append(company.get_text())

# print(len(companies), len(ratings))


data = {"Companies": companies, "Ratings": ratings}
dataframe = pd.DataFrame.from_dict(data)

# print(dataframe)



mean_values = dataframe.groupby("Companies").Ratings.mean()
ten_best = mean_values.nlargest(10)

print(ten_best)


