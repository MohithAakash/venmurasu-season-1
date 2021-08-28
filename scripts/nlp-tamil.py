from rippletagger.tagger import Tagger
import pandas as pd
import csv
from pprint import pprint

# POS tagging
tagger = Tagger(language="tam")

def get_data():

    df= pd.read_csv('../data/merged/sentences.csv')

    df = df.dropna()

    data = []

# Iterate over each row
    for index, row in df.iterrows():

        query = row['வாக்கியங்கள்']
        query = ''.join( c for c in query if c not in "”“‘’'\",.[]!?/…" )

        posTagger = tagger.tag(query)
        data += posTagger
        
    df = pd.DataFrame(data, columns=['Word', 'Part of Speech'])
    df.to_csv('parts-of-speech.csv', index=False)

if __name__ == "__main__":
    get_data()

