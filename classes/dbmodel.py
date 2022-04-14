import sqlite3
import os
from typing import Callable, List
import pandas as pd

class SimpleQueryFuncs:
    DEFAULT_COLUMNS = 'id, name, language, type, status, premiered'
    
    def query_all_movies(self):
        df = pd.read_sql_query(f'SELECT {SimpleQueryFuncs.DEFAULT_COLUMNS} FROM {self.tb_name}', self.conn)
        return df
    
    def query_movie_by_id(self, id: int):
        df = pd.read_sql_query(f'SELECT {SimpleQueryFuncs.DEFAULT_COLUMNS} FROM {self.tb_name} WHERE id = {id}', self.conn)
        return df

    def delete_movie_by_id(self, id: int):
        self.c.execute(f'DELETE FROM {self.tb_name} WHERE id = {id}')
        self.conn.commit()
    
    def delete_all_movies(self):
        self.c.execute(f'DELETE FROM {self.tb_name}')
        self.conn.commit()

    def id_exists(self, id: int):
        self.c.execute(f'SELECT id FROM {self.tb_name}')
        if (id,) in self.c.fetchall():
            return True
        return False

    def amount_of_records(self):
        self.c.execute(f'SELECT * FROM {self.tb_name}')
        return len(self.c.fetchall())
    

class DatabaseModel(SimpleQueryFuncs):
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
        
        for i in obj:
            if isinstance(obj[i], dict):
                for j in obj[i]:
                    if (isinstance(obj[i][j], dict) and 'href' in obj[i][j]):
                        for l in obj[i][j]:
                            ls_of_all.append(obj[i][j]['href'])
                    else:
                        ls_of_all.append(obj[i][j])
            else:
                ls_of_all.append(obj[i])


        self.__insert_into_db(ls_of_all)

    def __insert_into_db(self, ls: List) -> None:
        
        try:
            # Casting
            ls[5] = str(ls[5])
            ls[13] = str(ls[13])
            ls[18] = str(ls[18])
            ls[19] = str(ls[19])
                    
            # To tuple
            ls_new = [tuple(ls)]
            self.c.executemany(f'INSERT INTO {self.tb_name} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ls_new)
            self.conn.commit()
            
        except sqlite3.ProgrammingError:
            for i in range(31 - len(ls)):
                ls.append(None)
                
            ls_new = [tuple(ls)]
            self.c.executemany(f'INSERT INTO {self.tb_name} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ls_new)
            self.conn.commit()
            
            
if __name__ == '__main__':
    db = DatabaseModel(db_dir=f'{os.getcwd()}\\data')

