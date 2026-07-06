import requests
from bs4 import BeautifulSoup #this is a library that allows us to parse HTML and XML documents.
import pandas as pd

url = "https://www.safaribookings.com/tours/kenya/lodge"

response = requests.get(url, timeout=10)

print(response.status_code)
#print(response.text[:500]) this will print the first 500 characters of the HTML response

soup = BeautifulSoup(response.text, 'html.parser') 

titles = soup.find_all("div", class_="holder-tourtitle")

print(f"i found {len(titles)} tours")

data = []


for title in titles:
    safari = {
        "title": title.get_text(strip=True),
    } #this will create a dictionary with the title of the safari tour
    
    data.append(safari) #this will append the dictionary to the data list
    
df = pd.DataFrame(data) #this will create a dataframe from the data list

df.to_csv("safari_tours.csv", 
          index=False) #this will save the dataframe to a csv file without the index column

print(f"saved {len(data)} safari tours to safari_tours.csv")
    
    