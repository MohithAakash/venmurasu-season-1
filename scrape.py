from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from pprint import pprint
import csv

# page = requests.get(url)

# soup = BeautifulSoup(page.content, "html.parser")

def get_data(url,i):
    driver = webdriver.Chrome(executable_path='/home/mohith/selenium_driver/chromedriver')
    # driver.minimize_window()
    driver.get(url)
    # time.sleep(15)
    html = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(html,"html.parser")
    driver.quit()

    results = soup.select('.content p')
    print(len(results))

    csvfile = open(f"chpt{i}.csv", 'w')
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(["வார்த்தைகள்"])


    for i in range(len(results)):
        if i not in [0,1,5,6]:
            for j in results[i].text.split():
                print([j])
                csvwriter.writerow([j])
    # f.write(result.text)

for i in range(1,6):
    url = f"https://venmurasu.in/mutharkanal/chapter-{i}/"
    get_data(url,i)



# from itertools import zip_longest
# item1 = ['toys', 'ball', 'cot']
# item2 = ['fan', 'goat', 'ink', 'jug']
# data = [item1, item2]
# export_data = zip_longest(*data, fillvalue = '')
# for d in export_data:
#     print
