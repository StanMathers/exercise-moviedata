from classes.dbmodel import *
from classes.requestdata import *
from classes.shortcutfuncs import *


def main():
    req = RequestToMaze()
    db = DatabaseModel()
    sh = ShortcutFuncs()
    
    db.extact_and_parse_data(req.send_request)


if __name__ == '__main__':
    main()


