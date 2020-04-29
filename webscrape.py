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

print(ratings)

