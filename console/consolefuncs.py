from termcolor import colored

def display_options(db_model):
    print(colored(f'\nAmount of record in database: {db_model.amount_of_records()}\n', 'green'))
    print(f'1. Search movie\n2. Query all movies\n3. Query movie by ID\n4. Delete movie by ID\n{colored("0. Exit", "red")}')

# Subfunctions

# Search movie
def search_movies(request_model, db_model):
    while True:
        category = input('Movie category: ')
        request_model.update_query_string(category)
        
        if db_model.id_exists(request_model.first_movie_id()) == False:
            ask_for_download(request_model, db_model)
            break
        else:
            print(colored('\nMovie was found in a database.\n', 'green'))
            print(db_model.query_movie_by_id(request_model.first_movie_id()))
            break

def ask_for_download(request_model, db_model):
    while True:
        print('')
        
        enter_cmd = input(colored('Movie was not found in database. Would you like to download it? y/n: ', 'red')).lower()
        if enter_cmd == 'y':
            db_model.extact_and_parse_data(request_model.send_request)
            print(db_model.query_movie_by_id(request_model.first_movie_id()))
            print(colored('Movie was downloaded from website and saved to database', 'green'))
            break

        elif enter_cmd == 'n':
            break
        
# Query
def query_all_movies(db_model):
    print(db_model.query_all_movies())


# Query by ID
def query_by_id(db_model):
    while True:
        try:
            movie_id = int(input('Movie ID: '))
            if db_model.id_exists(movie_id):
                print('')
                db_model.query_movie_by_id(movie_id)
                break
            else:
                print('Wrong ID')
            
        except ValueError:
            print('Wrong type of data')
        
        except KeyboardInterrupt:
            break


def delete_movie_by_id(db_model):
    while True:
        try:
            movie_id = int(input('Movie ID: '))
            if db_model.id_exists(movie_id):
                print('')
                print(db_model.delete_movie_by_id(movie_id))
                print('Movie was deleted successfully')
                break
            else:
                print('Wrong ID')
            
        except ValueError:
            print('Wrong type of data')

        except KeyboardInterrupt:
            break











