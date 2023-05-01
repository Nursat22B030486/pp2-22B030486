import psycopg2


if __name__ == "__main__":
    connection = None

    try:
        connection = psycopg2.connect(host='localhost', user='postgres', dbname='phone_book', password='i_believe')
        cursor = connection.cursor()
        connection.autocommit = True
        
        query = """DROP PROCEDURE insert;"""
        query_1 = """DROP PROCEDURE update;"""
        query_2 = """DROP PROCEDURE insert_by_list;"""
        query_3 = """DROP PROCEDURE delete;"""
        cursor.execute(query)
        cursor.execute(query_1)
        cursor.execute(query_2)
        cursor.execute(query_3)

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"You have a problem!!!!!\n {error}")
    finally:
        if connection is not None:
            connection.close()
        print("All queries have done successfully!!!")
