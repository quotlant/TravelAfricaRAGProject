import pandas as pd
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

#reading the cleaned data from the csv file
df = pd.read_csv("data/safari_tours_clean.csv")


client = chromadb.PersistentClient(
    path = "data/chromadb"
)  #client is the connection to the chromadb database, and the path is where the database will be stored


#creating the embedding model 
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = client.get_or_create_collection(
    name = "safari_tours",
    embedding_function = embedding_function
) #this will create a collection in the chromadb database with the name "safari_tours" and the embedding function defined above

#add the data to the collection

if collection.count() == 0:
    collection.add(
        documents = df["search_text"].tolist(),
        ids = [str(i) for i in range(len(df))],
        metadatas = df[["country", "title", "details", "operator"]].to_dict(orient="records") 
    )

#print(collection.count()) #this will print the number of documents in the collection


#this function will search the safari tours based on the query and return the top_k results. top_k is the number of results to return. The default value is 5. 
def search_safaris(query, top_k=5):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    
    return results 
