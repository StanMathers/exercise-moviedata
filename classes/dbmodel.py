import sqlite3
import os
from typing import Callable, List, Any
from pprint import pprint

class DatabaseModel:
    def __init__(self, db_dir: str = f'{os.getcwd()}\\classes\\data', db_name: str = 'moviedata.db', tb_name: str = 'moviedetails'):
        self.db_dir = db_dir
        self.db_name = db_name
        self.tb_name = tb_name
        
        self.conn = sqlite3.connect(f'{self.db_dir}\\{self.db_name}')
        self.c = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.c.execute(f'''
                       CREATE TABLE IF NOT EXISTS {self.tb_name}(
                           id INT UNIQUE,
                           url STRING,
                           name STRING,
                           type STRING,
                           language STRING,
                           genres STRING,
                           status STRING,
                           runtime FLOAT,
                           averageTime FLOAT,
                           premiered DATE,
                           ended DATE,
                           officialSite STRING,
                           time STRING,
                           days STRING,
                           average STRING,
                           weight INT,
                           network STRING,
                           network_id INT,
                           network_name STRING,
                           country STRING,
                           officialSite2 STRING,
                           dvdCountry STRING,
                           tvrage STRING,
                           thetvdb STRING,
                           imdb FLOAT,
                           medium STRING,
                           original STRING,
                           summary STRING,
                           updated INT,
                           self STRING,
                           previousepisode STRING
                       )
                       ''')
        self.conn.commit()
        
    def extact_and_parse_data(self, class_obj: Callable):
        ls_of_all = []
        obj = class_obj()
        id_check = 0
        for i in obj:
            if i == 'id': id_check += 1
            
            if isinstance(obj[i], dict):
                for j in obj[i]:
                    if (isinstance(obj[i][j], dict) and 'href' in obj[i][j]):
                        for l in obj[i][j]:
                            ls_of_all.append(obj[i][j]['href'])
                    else:
                        ls_of_all.append(obj[i][j])
            else:
                ls_of_all.append(obj[i])
        
        # Casting
        ls_of_all[5] = str(ls_of_all[5])
        ls_of_all[13] = str(ls_of_all[13])
        ls_of_all[19] = str(ls_of_all[19])
                
        # To tuple
        ls_of_all = [tuple(ls_of_all)]
        self.c.executemany(f'INSERT INTO {self.tb_name} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ls_of_all)
        self.conn.commit()
        
if __name__ == '__main__':
    db = DatabaseModel(db_dir=f'{os.getcwd()}\\data')

