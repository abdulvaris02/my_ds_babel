import sqlite3 as sql 
import csv
import pandas as pd



def sql_to_csv(database, table_name):
    database = sql.connect(database)
    navigator = database.cursor()
    navigator.execute(f"SELECT * FROM {table_name};")
    heads = [each[0] for each in navigator.description]
    # head = str(heads)[:]
    # print(head)
    # lst = [head]
    # for i in navigator:
    #     lst.append(str(list(i))[:])
    #     lst.append('\n')
    
    
    with open("list_fault_lines.csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(heads)
        writer.writerows(navigator)
    database.commit()
    database.close() 
    
    with open("list_fault_lines.csv", 'r') as out_file:
        return out_file.read().rstrip()
        
    # return ''.join(lst)


def csv_to_sql(csv_content, database_name, table_name_1):
    connection = sql.connect(database_name)
    navigator = connection.cursor()
    data = pd.read_csv(csv_content)   
    df = pd.DataFrame(data)
    df.to_sql(table_name_1, connection, if_exists='replace', index = False)
