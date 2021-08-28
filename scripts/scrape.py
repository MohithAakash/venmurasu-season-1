from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from pprint import pprint
import csv

driver = webdriver.Chrome(executable_path='/home/mohith/selenium_driver/chromedriver')

def get_data(url,i):
    
    # driver.minimize_window()
    driver.get(url)
    # time.sleep(15)
    html = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(html,"html.parser")

    results = soup.select('.content p')
    print(len(results))

    csvfile = open(f"sentences/chpt{i}.csv", 'w')
    csvwriter = csv.writer(csvfile) 
    # csvwriter.writerow(["வார்த்தைகள்"])
    csvwriter.writerow(["வாக்கியங்கள்"])

    for i in range(len(results)):
        if i not in [0,1,5,6]:
            # Splitting into words
            # for j in results[i].text.split():
            #     # print([j])
            #     csvwriter.writerow([''.join( c for c in j if c not in "”“‘’'\",.[]!?/… " )])

            # Splitting into sentences
            for j in results[i].text.split('.'):
                print([j])
                csvwriter.writerow([j])



# def get_sentences():

for i in range(1,6):
    url = f"https://venmurasu.in/mutharkanal/chapter-{i}/"
    get_data(url,i)
    
driver.quit()

# j = "\"கொள்கிறேன்,\""
# print(''.join( c for c in j if c not in "'\"," ))


# from itertools import zip_longest
# item1 = ['toys', 'ball', 'cot']
# item2 = ['fan', 'goat', 'ink', 'jug']
# data = [item1, item2]
# export_data = zip_longest(*data, fillvalue = '')
# for d in export_data:
#     print
