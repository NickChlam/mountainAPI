import pyodbc 
import textwrap
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Thirteener:
    def __init__(self, coRank, rank, peak, elevation, ranges):
        self.coRank = coRank
        self.rank = rank
        self.peak = peak
        self.elevation = elevation
        self.ranges = ranges
        

    def toString(self):
        print(self.coRank + ' ' + self.rank + ' ' + self.peak + ' ' + self.elevation + ' ' + self.ranges)

class Mountains:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1400,650')
        options.add_argument('headless')
        self.bot = webdriver.Chrome(options=options)
        self.thirteeners = []
    
    
    
    def getMountains(self):
        peaks = []
        index = 1
        arrIndex = 0
        coRank = ''
        rank = ''
        peak = ''
        elevation = ''
        ranges = ''

        bot = self.bot
        bot.get('https://www.14ers.com/13ers/13ers.php?displaytype=0&sublist=13ers&listd=list')
        table = bot.find_element_by_id('resultsTable2')

        rows = table.find_elements_by_tag_name('tr')

        for data in rows:
            items = data.find_elements_by_tag_name('td')
            index = 0
            
            for item in items:
                index += 1
                if index == 1:
                    #if item.text != '':
                    coRank = item.text
                    
                if index == 2: 
                    #if item.text != '':
                    rank = item.text
                if index == 4:
                    #if item.text !='':
                    peak = item.text
                    
                if index == 5:
                    #if item.text != '':
                    elevation = item.text
                if index == 6:
                    #if item.text != '':
                    ranges = item.text

                if index == 8:
                    self.thirteeners.append(Thirteener(coRank, rank, peak, elevation, ranges))
                    print(self.thirteeners[arrIndex].toString())
                    arrIndex +=1
                    

scrape = Mountains()

scrape.getMountains()



for item in scrape.thirteeners:
    print(item.coRank + ' ' + item.peak + ' ' + item.elevation + ' ' + item.ranges)

try:
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=54.237.212.134;'
                      'Database=mountains;'
                      'UID=SA;'
                      'PWD=!Dickhead123;')

    print('connection succeful')
except Exception as ex:
    print(ex)

cursor = conn.cursor()

for item in scrape.thirteeners:
    print(item.rank)
    query = textwrap.dedent(f'''
        INSERT INTO mountains.dbo.thirteeners (coRank, ranked, peak, elevation, ranges)
        VALUES ('{item.coRank}', '{item.rank}', '{item.peak}', '{item.elevation}'', '{item.ranges}');
    ''')
    cursor.execute(query)
    conn.commit()

conn.close()

