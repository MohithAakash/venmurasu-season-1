import pandas as pd
import csv
from tamil import utf8
import os

def freq():

    df = df.pivot_table(columns=['வார்த்தைகள்'], aggfunc='size')
    print(df)

    df.to_csv('data.csv', encoding='utf-8')

def most_freq(df):
    # df = df.mode()
    df = df['வார்த்தைகள்'].value_counts()
    print(df)
    df.to_csv('mostfreq.csv', encoding='utf-8')

def sentences():
    new = df.dropna()
    new.to_csv('dummy.csv')

def count_letters():
    f= open("dummy.csv","w")
    csvwriter = csv.writer(f) 

    for index, row in df.iterrows():
        letters = utf8.get_letters(row['வார்த்தைகள்'])
        letter_count = utf8.get_letters_length( row['வார்த்தைகள்'] )
        letters.insert(0,letter_count)
        print(letters)
        csvwriter.writerow(letters)

def split_letters():
    # print(utf8.splitMeiUyir('வார்'))
    # print(utf8.calculate_maththirai('வார்த்தைகள்'))
    print(utf8.splitMeiUyir('வா'))

def mathirai():
    list_of_files = [sorted(os.listdir("../data/sentences"))]

    i=1

    main_df = pd.DataFrame()

    for file in list_of_files[0]:

        df= pd.read_csv('../data/words/' + file)

        df["Chapter"] = "Chapter-" + str(i)
        # if i == 3:
            # print(df.dtypes)
        # try:
        df["Mathirai"] = df['வார்த்தைகள்'].apply(lambda x: utf8.calculate_maththirai(str(x)))
        # except:
        #     df["Mathirai"] = ""
        # m = utf8.calculate_maththirai('வார்த்தைகள்')
        # pd.concat([main_df , df])
        print(df)
        i+=1



        df.to_csv("test2.csv", header=None, mode='a', index=False)

def count():
    df = pd.read_csv('../data/merged/' + 'sentences.csv')
    print(df)



if __name__ == "__main__":

    # most_freq()
    mathirai()



