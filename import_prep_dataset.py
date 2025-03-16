"""
* Name         : import_prep_dataset.py
* Author       : E Wilber
* Created      : 02/16/25
* Module       : 5
* Topic        : 1 and 2
* Description  : Import and Prep Dataset
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import pandas as pd

#Loads dataset
file_path = 'steam.csv'
df = pd.read_csv(file_path)
#Groups by publisher and sum of positive ratings
temp_df = df.groupby('publisher', as_index=False)['positive_ratings'].sum()
#Identifys publishers with< 50 positive ratings
publishers_to_remove = temp_df[temp_df['positive_ratings'] < 50]['publisher'].tolist()
#Creates new dataframe excludig these publishers
filtered_df = df[~df['publisher'].isin(publishers_to_remove)]
#Sorts by positive ratings, descending
filtered_df = filtered_df.sort_values(by='positive_ratings', ascending=False)
#Displays quick statistics
describe_stats = filtered_df.describe()
print("-" * 70)
print("QUICK STATS")
print("-" * 70)
print(describe_stats)
print("-" * 70)
#Removes appid column using iloc
filtered_df = filtered_df.iloc[:, 1:]
#Removes games with< 20,000 owners
filtered_df = filtered_df[filtered_df['owners'].str.split('-').str[0].str.replace(',', '').astype(int) >= 20000]
#Shows 1st few rows
print("-" * 70)
print("GAMES WITH < 20,000 OWNERS")
print("-" * 70)
print(filtered_df.head())
print("-" * 70)
#Creates frame including owners, positive ratings, negative ratings
owners_df = df[['owners', 'positive_ratings', 'negative_ratings']]
#Groups by owners and sum
owners_grouped = owners_df.groupby('owners').sum()
print("-" * 70)
print("SUMMED OWNERS")
print("-" * 70)
print(owners_grouped)
print("-" * 70)
#Adds percentage columns
owners_grouped['% positive reviews'] = owners_grouped['positive_ratings'] / (owners_grouped['positive_ratings'] + owners_grouped['negative_ratings'])
owners_grouped['% negative reviews'] = owners_grouped['negative_ratings'] / (owners_grouped['positive_ratings'] + owners_grouped['negative_ratings'])
print("-" * 70)
print("GAME RATINGS")
print("-" * 70)
print(owners_grouped)
print("-" * 70)
#Desending by positive rating
owners_grouped = owners_grouped.sort_values(by='% positive reviews', ascending=False)
#Creates frame with publisher, positive ratings, and negative ratings
publishers_df = df[['publisher', 'positive_ratings', 'negative_ratings']]
#Groups by publisher and sum
publishers_grouped = publishers_df.groupby('publisher').sum()
#Adds percentage columns
publishers_grouped['% positive reviews'] = publishers_grouped['positive_ratings'] / (publishers_grouped['positive_ratings'] + publishers_grouped['negative_ratings'])
publishers_grouped['% negative reviews'] = publishers_grouped['negative_ratings'] / (publishers_grouped['positive_ratings'] + publishers_grouped['negative_ratings'])
#descending by positive reviews
publishers_grouped = publishers_grouped.sort_values(by='% positive reviews', ascending=False)
print("-" * 70)
print("PUBLISHER RATINGS")
print("-" * 70)
print(publishers_grouped)
print("-" * 70)
#Drops publishers with< 1000 positive rating
publishers_grouped = publishers_grouped[publishers_grouped['positive_ratings'] >= 1000]
#Drops publishers with< 5 games
publishers_grouped = publishers_grouped[publishers_grouped.index.map(lambda x: (df['publisher'] == x).sum() >= 5)]
print("-" * 70)
print("PUBLISHERS with over 1000 POSITIVE RATINGS and more than 5 GAMES")
print("-" * 70)
print(publishers_grouped)
print("-" * 70)
