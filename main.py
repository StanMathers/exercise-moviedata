from classes.dbmodel import *
from classes.requestdata import *
from console.consolefuncs import *


def main():
    req = RequestToMaze()
    db = DatabaseModel()

    while True:
        display_options(db)
        
        try:
            enter_command = int(input('>>>'))
            if enter_command == 0:
                exit()
        
            elif enter_command == 1:
                search_movies(req, db)
            
            elif enter_command == 2:
                query_all_movies(db)

            elif enter_command == 3:
                query_by_id(db)
            
            elif enter_command == 4:
                delete_movie_by_id(db)
            
            elif enter_command == 5:
                trunc_table(db)
            
        except ValueError:
            print('\nWrong type of data')
        except KeyboardInterrupt:
            exit()
    
if __name__ == '__main__':
    main()


