import psycopg2
# from config import config

def create_table():
    table = """
        CREATE TABLE data_snake(
            id SERIAL NOT NULL,
            user_name VARCHAR(55) NOT NULL,
            user_level INTEGER,
            user_score INTEGER,
            user_speed INTEGER,
            PRIMARY KEY (id)
        );
    """

    connection = None

    try:
        # param = config()
        # connection = psycopg2.connect(**param)
        connection = psycopg2.connect(
                                host = 'localhost',
                                dbname = 'data_of_snake',
                                user = 'postgres',
                                password = 'i_believe')
        cursor = connection.cursor()
        cursor.execute(table)
        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f" We found error as {error}")
    finally:
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    create_table()