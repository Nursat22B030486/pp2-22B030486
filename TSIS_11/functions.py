import psycopg2


if __name__ == "__main__":
    
    connection = None

    try:
        connection = psycopg2.connect(host='localhost', user='postgres', dbname='phone_book', password='i_believe')
        cursor = connection.cursor()
        connection.autocommit = True
        
        function_name = f"""
            CREATE OR REPLACE FUNCTION search_name(pattern VARCHAR)
            RETURNS TABLE (Names VARCHAR, numbers VARCHAR, pos VARCHAR)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                RETURN QUERY SELECT first_name, phone_number, status FROM phone_book WHERE first_name ~~* pattern;
            END;
            $$
        """
        
        function_phone = f"""
            CREATE OR REPLACE FUNCTION search_phone(pattern VARCHAR)
            RETURNS TABLE (Names VARCHAR, numbers VARCHAR, pos VARCHAR)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                RETURN QUERY SELECT first_name, phone_number, status FROM phone_book WHERE  phone_number ~~ pattern;
            END;
            $$
        """

        function_pagination = """
        CREATE OR REPLACE FUNCTION pagination(number INTEGER, amount INTEGER)
        RETURNS TABLE (name VARCHAR, numbers VARCHAR)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            RETURN QUERY SELECT first_name, phone_number FROM phone_book OFFSET number LIMIT amount;
        END;
        $$
        """
        # ~ '^.*pattern.*$'
        cursor.execute(function_name)
        cursor.execute(function_phone)
        cursor.execute(function_pagination)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"You have a problem!!!!!\n {error}")
    finally:
        if connection is not None:
            connection.close()
        print("All queries have done successfully!!!")