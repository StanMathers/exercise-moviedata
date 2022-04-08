import sqlite3
import os
from typing import Callable

class DatabaseModel:
    def __init__(self, db_dir: str = f'{os.getcwd()}\\classes\\data', db_name: str = 'moviedata.db', tb_name: str = 'moviedetails'):
        self.db_dir = db_dir
        self.db_name = db_name
        self.tb_name = tb_name
        
        # self.conn = sqlite3.connect(f'{self.db_dir}\\{self.db_name}')
        # self.c = self.conn.cursor()

    def extact_and_parse_data(self, class_obj: Callable):
        obj = class_obj()
        id_check = 0
        for i in obj:
            if i == 'id': id_check += 1

            # If dictionary is in another dict then loop it
            if isinstance(obj[i], dict):
                
                # Loop the second dict in a dict
                for j in obj[i]:
                    
                    # If id was already used the rename it to id2
                    if id_check == 1 and j == 'id':
                        print(f'id2 - {obj[i][j]}')
                    else:
                        print(f'{j} - {obj[i][j]}')
            
            # Otherwise just loop first loop
            else:
                print(f'{i} - {obj[i]}')



db = DatabaseModel()



