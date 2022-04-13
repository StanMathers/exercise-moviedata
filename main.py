from classes.dbmodel import *
from classes.requestdata import *
from classes.shortcutfuncs import *
from console.consolefuncs import *


def main():
    req = RequestToMaze()
    db = DatabaseModel()
    sh = ShortcutFuncs()

    while True:
        display_options(db)
        
        enter_command = input('>>>')
        if enter_command == '0':
            exit()
        
        elif enter_command == '1':
            search_movies(req, db)
        
        elif enter_command == '2':
            query_all_movies(db)

    
if __name__ == '__main__':
    main()


