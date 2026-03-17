import pandas as pd

df = pd.read_csv("dataset/kdrama.csv")

print(df.head())
print(df.info())

#DATA CLEANING
# removing useless index column
df = df.drop(columns=['Unnamed: 0'])

# rename columns for easier use
df.columns = [
    'Drama_Name',
    'Year',
    'Genre',
    'Main_Cast',
    'Synopsis',
    'Rating',
    'Content_Rating',
    'Tags',
    'Network',
    'Image_URL',
    'Episodes'
]

# converting rating to numeric
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# extracting episode number from text like "16 episodes"
df['Episodes'] = df['Episodes'].str.extract('(\d+)').astype(float)

# converting year to integer
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# removing missing ratings
df = df.dropna(subset=['Rating'])

# removing duplicates
df = df.drop_duplicates()

print(df.describe())

#EDA- EXPLORATORY DATA ANALYSIS-
#Popular Genre
genre_counts = df['Genre'].value_counts().head(10)
print(genre_counts)  

#Kdrama Production Trend
year_trend = df['Year'].value_counts().sort_index()
print(year_trend) 
top_rated = df.sort_values(by='Rating', ascending=False).head(10)

#TopratedDrama
top_rated = df.sort_values(by='Rating', ascending=False).head(10)

print(top_rated[['Drama_Name','Rating']])

#distribution of network
network_counts = df['Network'].value_counts().head(10)

print(network_counts)

#clean dataset saving
df.to_csv("dataset/kdrama_clean.csv", index=False)