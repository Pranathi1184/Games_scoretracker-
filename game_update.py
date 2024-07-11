import sys
import pymysql

def get_connection():
    conn = pymysql.Connect(
        host='localhost', port=3306,
        user='root', password='pranathi@110804',
        db='Gaming', charset='utf8')
    return conn
def insert():
    username = input('Enter User name: ')
    level_no= input('Enter level no : ')
    friends_list = input('Enter friends list: ')
    score = input('Enter the score : ')

    conn = get_connection()
    my_cursor = conn.cursor()   
    insert_query = """insert into details(username, level_no, friends_list, score) values(%s, %s, %s, %s)"""

    gaming_details_record = (username, level_no, friends_list, score)
    my_cursor.execute(insert_query, gaming_details_record) 
    conn.commit()
    my_cursor.close()
    conn.close()
    return "Successfully inserted a row"
def search_one():
    username = input('Enter Username to search record: ')
    conn = get_connection()
    search_query = """ select * from details where username = %s"""
    my_cursor = conn.cursor()
    my_cursor.execute(search_query, username)

    row_data = my_cursor.fetchone()
    if row_data == None:
        return 'Username:{} not found'.format(username)
    print(f'Username details are: ')
    print(str(row_data))
    return '\n Username: {} details displayed successfully'.format(username)


def print_records(rows):
    print('%-10s %-15s %-18s %-10s %-10s %-10s'%("USER_ID", "USERNAME", "LEVEL_NO", "FRIENDS_LIST", "SCORE", "LOGIN_DATE"))

    for row in rows:
        print('%10s %-20s %-35s %-10s %11s %5s'%(row[0], row[1], row[2], row[3], row[4], row[5]))
  
def list_all():
    conn = get_connection()
    my_cursor = conn.cursor()
    sql_query = 'select * from details'
    my_cursor.execute(sql_query)
    table_data = my_cursor.fetchall()
    if table_data == None:
        return 'No rows available in the table'
    my_cursor.close()
    conn.close()

    print_records(table_data)
    return 'All records fetched and printed successfully'

def update_one():
    username = input('Enter Username to update the record: ')
    new_level = input('Enter the level no to be updated: ')
    new2_score = input('Enter the score to be updated ')

    my_connection = get_connection()
    my_cursor = my_connection.cursor()

    update_query = """update details set level_no=%s, score=%s where username=%s"""
    new_data = (new_level, new2_score, username)
    my_cursor.execute(update_query, new_data) 
    my_connection.commit()
    my_cursor.close() 
    my_connection.close()
    if my_cursor.rowcount == 1:
        return 'Record updated and saved successfully'
    else:
        return 'Record with Name: {} not found'.format(username)

def delete_one():
    username = input('Enter username of the gamer to delete the record: ')

    my_connection = get_connection()
    my_cursor = my_connection.cursor()

    delete_query = """delete from details where username=%s"""
    my_cursor.execute(delete_query, username) 
    my_connection.commit()
    my_cursor.close() 
    my_connection.close()
    if my_cursor.rowcount == 1:
        return 'Record with name:{} deleted successfully'.format(username)
    else:
        return 'Record with name: {} not found'.format(username)

def exit_program():
    sys.exit('End of program')

def invalid_choice():
    return 'Invalid choice entered'

def start_app():
    crud_options = {
        1 : insert,
        2 : search_one,
        3 : list_all,
        4 : update_one,
        5 : delete_one,
        6 : exit_program
    } 
    count_of_oprs = 10
    while count_of_oprs >= 1:
        print('1:Insert 2:Search 3:Display 4:Update 5:Delete 6:Exit')
        choice = int(input('Your choice please: '))
        print(crud_options.get(choice, invalid_choice)())
        count_of_oprs -= 1
    print('End of program') 
start_app()