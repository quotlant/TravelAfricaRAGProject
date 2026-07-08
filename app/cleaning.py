import pandas as pd

#load scraped data from csv file
df = pd.read_csv("data/safari_tours.csv")


#print(df.head()) #this will print the first 5 rows of the dataframe
print(df.shape) #this will print the number of rows and columns in the dataframe

df = df.drop_duplicates() #this will drop duplicate rows from the dataframe

print(df.isnull().sum()) #this will print the number of missing values in each column


#drop rows with missing values in the title column
df = df.dropna(subset=["title"]) #this will drop rows with missing values in the title column

#remove extra whitespace from the title column
df["title"] = df["title"].str.strip() #this will remove extra whitespace from.
df["details"] = df["details"].str.strip() #this will remove extra whitespace from the details column
df["operator"] = df["operator"].str.strip() #this will remove extra whitespace from

#create a text column for embedding
df["search_text"] = (
    "Safari Title: " + df["title"] + 
    "\nDetails: " + df["details"] +
    "\nOperator: " + df["operator"]
    
)
print("After Cleaning")
print(df.shape)

df.to_csv("data/safari_tours_clean.csv",
          index=False)

print("Saved Clean Data")