import requests
from bs4 import BeautifulSoup #this is a library that allows us to parse HTML and XML documents.
import pandas as pd



safaris = []
countries = [
    "kenya",
    "tanzania",
    "uganda",
    "rwanda",
    "south-africa",
    "botswana"
]

for country in countries:
    print(f"\nScraping {country.title()}...")
    for page in range(1,4):
        if page == 1:
            url = f"https://www.safaribookings.com/tours/{country}/lodge"
        else:
            url = f"https://www.safaribookings.com/tours/{country}/lodge/page/{page}"
        
        print(f"Scraping page {page} of safari tours...")
        
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page} of safari tours for {country.title()}. Status code: {response.status_code}")
            continue
            

        soup = BeautifulSoup(response.text, 'html.parser') 

        titles = soup.find_all("div", 
                            class_="holder-tourtitle")
        print(f"Found {len(titles)} safari tours on page {page} for {country.title()}.")

        details = soup.find_all( "div",
                                class_= "list__item--data" 
        )

        operators = soup.find_all("div",
                                class_="operator-snippet__data"
                                )



        for i in range(len(titles)):
            safari = {
                "country": country.title(),
                
                "title": titles[i].get_text(" ", strip=True),
            #this will create a dictionary with the title of the safari tour
            "details": (details[i].get_text(" ", strip=True)
            if i < len(details)
            else ""
            ),
            
            "operator": (operators[i].get_text(" ", strip=True)
            if i < len(operators)
            else ""
            ),
            
            }
            safaris.append(safari) #this will append the dictionary to the data list
            
df = pd.DataFrame(safaris) #this will create a dataframe from the data list
df.to_csv("data/safari_tours.csv", 
          index=False) #this will save the dataframe to a csv file without the index column

print(f"saved {len(safaris)} safari tours to safari_tours.csv")


    
    