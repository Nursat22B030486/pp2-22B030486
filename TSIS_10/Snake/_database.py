import psycopg2
# from config import config

def does_exists(username):
    # param = config()
    connection = psycopg2.connect(
                                host = 'localhost',
                                dbname = 'data_of_snake',
                                user = 'postgres',
                                password = 'i_believe')

    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM data_snake""")
    rows = cursor.fetchall()

    for row in rows:
        if row[1] == username:
            return True 
    return False
    
def show_previous_result(username):
    # param = config()
    # connection = psycopg2.connect(**param)
    connection = psycopg2.connect(
                                host = 'localhost',
                                dbname = 'data_of_snake',
                                user = 'postgres',
                                password = 'i_believe')
    cursor = connection.cursor()

    cursor.execute(F"""SELECT * FROM data_snake""")
    rows = cursor.fetchall()
    for row in rows:
        if username == row[1]:
            print(f"""
                  User_name - {row[1]}
                  Level - {row[2]}
                  Score - {row[3]}
                  Speed - {row[4]} """)
    
    # print(cursor.fetchone())
    cursor.close()
    connection.close()


def  inserting_data(name, level, score, speed):
    
    data = """
        INSERT INTO data_snake (user_name, user_level, user_score, user_speed) 
        VALUES (%s, %s, %s, %s)
    """

    # params = config()
    # connection = psycopg2.connect(**params)
    connection = psycopg2.connect(
                                host = 'localhost',
                                dbname = 'data_of_snake',
                                user = 'postgres',
                                password = 'i_believe')
    cursor = connection.cursor()
    connection.autocommit = True
    cursor.execute(data, (name, level, score, speed))

    cursor.close()
    connection.close()

def update_data(level, score, speed, name):
    # param = config()
    # connection = psycopg2.connect(**param)
    connection = psycopg2.connect(
                                host = 'localhost',
                                dbname = 'data_of_snake',
                                user = 'postgres',
                                password = 'i_believe')
    connection.autocommit = True
    cursor = connection.cursor()
    query = f"""UPDATE data_snake SET
                    user_level = '{level}',
                    user_score = '{score}',
                    user_speed = '{speed}'
                WHERE user_name = '{name}'              
    """

    cursor.execute(query, (level, score, speed, name))
    cursor.close()
    connection.close()



