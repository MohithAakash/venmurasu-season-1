import pandas as pd
import os

def merge():

    list_of_files = [sorted(os.listdir("../data/sentences"))]

    # print(list_of_files[0][49:])

    result_obj = pd.concat([pd.read_csv("../data/sentences/" + file) for file in list_of_files[0]])
    # Convert the above object into a csv file and export
    result_obj.to_csv("sentences.csv", index=False, encoding="utf-8")

merge()
