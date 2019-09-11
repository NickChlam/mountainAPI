import pyodbc 
import textwrap

class Thirteener:
    def __init__(self, coRank, rank, peak, elevation, ranges):
        self.coRank = coRank
        self.rank = rank
        self.peak = peak
        self.elevation = elevation
        self.ranges = ranges

name = 'nick'
thirteeners = []
thirteeners.append(Thirteener('2','12','pikes', '1200', 'sasquatch'))
thirteeners.append(Thirteener('3','14','longs', '12,4300', 'miamie'))
thirteeners.append(Thirteener('5','16','torreys', '14444', 'front'))

age = 34

print(thirteeners[0].ranges + ' ' +thirteeners[0].peak)

stuff = f'''your name is {name} and
 you are {age} years old'''

print(stuff)


try:
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=mountains.cdzitulendpj.us-east-1.rds.amazonaws.com;'
                      'Database=mountains;'
                      'UID=admin;'
                      'PWD=password;')

    print('connection succeful')
except Exception as ex:
    print(ex)

cursor = conn.cursor()

for item in thirteeners:
    print(item.rank)
    query = textwrap.dedent(f'''
        INSERT INTO mountains.dbo.thirteeners (coRank, ranked, peak, elevation, ranges)
        VALUES ('{item.coRank}', '{item.rank}', '{item.peak}', '{item.elevation}', '{item.ranges}');
    ''')
    print(query)
    cursor.execute(query)
    conn.commit()

conn.close()


        
        