import pymongo
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()

# Select database and collection
db = client.my_database
collection = db.my_collection

# Load dataframe
df = pd.read_csv('my_dataframe.csv')

# Convert dataframe to dictionary
data_dict = df.to_dict(orient='records')

# Insert dictionary into collection
collection.insert_many(data_dict)
Muluneh20:33
df.plot.scatter(x='x', y='y')
plt.show()