import psycopg2


if __name__ == "__main__":
    connection = None

    try:
        connection = psycopg2.connect(host='localhost', user='postgres', dbname='phone_book', password='i_believe')
        cursor = connection.cursor()
        connection.autocommit = True
        
        query = """DROP FUNCTION search_name;"""
        query_1 = """DROP FUNCTION search_phone;"""
        query_2 = """DROP FUNCTION pagination;"""
        cursor.execute(query)
        cursor.execute(query_1)
        cursor.execute(query_2)

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"You have a problem!!!!!\n {error}")
    finally:
        if connection is not None:
            connection.close()
        print("All queries have done successfully!!!")
