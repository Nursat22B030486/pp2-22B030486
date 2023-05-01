import psycopg2


if __name__ == "__main__":
    connection = None

    try:
        connection = psycopg2.connect(host='localhost', user='postgres', dbname='phone_book', password='i_believe')
        cursor = connection.cursor()
        connection.autocommit = True
    
        list_contact = ['Nobody', '77471598684', 'Unknown']#ARRAY('Sultan', '87474523562', 'KBTU'
        
        cursor.execute(f"""CALL insert_by_list ((ARRAY['(Sultan,87474523562,KBTU)'
                         ,'(Nobody,77471598684,Unknown)'])::info[]);""")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"You have a problem!!!!!\n {error}")
    finally:
        if connection is not None:
            connection.close()
        print("All queries have done successfully!!!")