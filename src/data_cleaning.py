import os
import pandas as pd


transcriptdf = pd.read_json(r'../data/transcript.json', lines=True)
portfoliodf = pd.read_json(r'../data/portfolio.json', lines=True)
profiledf = pd.read_json(r'../data/profile.json', lines=True)

profiledf = profiledf[
    (profiledf['gender'].notnull()) &
    (profiledf['age'] != 118) &
    (profiledf['income'].notnull())
]
profiledf.rename(columns={'id': 'person'}, inplace=True)

profiledf.to_csv(r'../data/cleaned_profile.csv')
