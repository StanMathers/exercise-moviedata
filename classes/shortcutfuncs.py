"""
ეს მოდული განსაკუთრებულს არაფერს აკეთებს, უბრალოდ მაგიდის შესაქმნელად პატარა სკრიპტია, რომელსაც დიქშენერიდან
მოაქვს column-ების სახელების ლისთი, რომელსაც შემდეგ მაგიდის შექმნისას გამოვიყენებ. უბრალოდ ხელით დაწერა დამეზარა
სათითაოდ და მაგიტომ გამოვყავი, თან ამის გამოკვეტება არ მინდოდა დანარჩენ ორში.
"""
from typing import List

class ShortcutFuncs:
    
    def get_table_column_list(self, class_obj) -> List:
        list_of_columns = []
        
        obj = class_obj()
        id_check = 0
        for i in obj:
            if i == 'id': id_check += 1

            if isinstance(obj[i], dict):
                for j in obj[i]:                    
                    if id_check == 1 and j == 'id':
                        list_of_columns.append('id2')
                    else:
                        list_of_columns.append(j)            
            else:
                list_of_columns.append(i)
        print(list_of_columns)         
        
        
        
        
'''
    def extact_and_parse_data(self, class_obj: Callable):
        ls_of_all = []
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

'''


'''
    def extact_and_parse_data(self, class_obj: Callable):
        ls_of_all = []
        obj = class_obj()
        id_check = 0
        for i in obj:
            if i == 'id': id_check += 1

            # If dictionary is in another dict then loop it
            if isinstance(obj[i], dict):
                
                # Loop the second dict in a dict
                for j in obj[i]:
                    
                    # If id was already used the rename it to id2
                    
                    # print(f'id2 - {obj[i][j]}')
                    ls_of_all.append(obj[i][j])
            
            # Otherwise just loop first loop
            else:
                # print(f'{i} - {obj[i]}')
                ls_of_all.append(obj[i])
        print(ls_of_all)

'''
