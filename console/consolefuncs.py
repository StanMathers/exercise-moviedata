

def display_options(db_model):
    print(f'\nAmount of record in database: {db_model.amount_of_records()}\n')
    print('1. Search movie\n2. Query all movies\n3. Query movie by ID\n4. Delete movie by ID\n0. Exit')

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
            print('\nMovie was found in a database.\n')
            print(db_model.query_movie_by_id(request_model.first_movie_id()))
            break

def ask_for_download(request_model, db_model):
    while True:
        print('')
        enter_cmd = input('Movie was not found in database. Would you like to download it? y/n: ').lower()
        if enter_cmd == 'y':
            db_model.extact_and_parse_data(request_model.send_request)
            print(db_model.query_movie_by_id(request_model.first_movie_id()))
            print('Movie was downloaded from website and saved to database')
            break

        elif enter_cmd == 'n':
            break
        
# Query
def query_all_movies(db_model):
    print(db_model.query_all_movies())
















