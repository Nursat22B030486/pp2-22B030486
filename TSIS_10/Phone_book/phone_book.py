import csv 
import psycopg2

def deleting_phone(username):
    cursor.execute(f"""DELETE FROM phone_book WHERE first_name = '{username}';""")


def insert_data():
    with open('data.csv', 'r') as file:
        data = csv.reader(file)
        for line in data:
            name = ("""INSERT INTO phone_book VALUES 
                (DEFAULT, %s, %s, %s);
            """)
            cursor.execute(name, line)

def query_filtering_id():
    cursor.execute("""SELECT * FROM phone_book WHERE id%2 = 0;""")
    for row in cursor.fetchall():
        print(row)

def query_filtering_range_and_in():
    cursor.execute("""SELECT * FROM phone_book WHERE (id between 4 and 6) AND (id in (3, 5, 7));""")
    for row in cursor.fetchall():
        print(row)

def query_order():
    cursor.execute("""SELECT first_name FROM phone_book ORDER BY first_name ASC;""")
    for row in cursor.fetchall():
        print(row)


connection = None

try:
    connection = psycopg2.connect(
        host="localhost",
        dbname="phone_book",
        user="postgres", 
        password="i_believe",
        port=5432
    )

    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("""SELECT version();""")
        print(f"Server version: {cursor.fetchone()}")


    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS phone_book(
                id serial PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(13) NOT NULL,
                status VARCHAR(15) NOT NULL
        );"""
        )
        # connection.commit()
        print("[INFO] Table is created succesfully")        
    
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO phone_book (id, first_name, phone_number, status) 
        VALUES
        (DEFAULT,'Nursat', '87474589586', 'family'),
        (DEFAULT,'Zhanserik', '87474574558', 'friend'),
        (DEFAULT, 'Nurzat', '87073071821', 'family'),
        (DEFAULT, 'Alinur', '87054540072', 'KBTU'),
        (DEFAULT, 'Mama', '87473610235', 'family'),
        (DEFAULT, 'Stranger', '87056384545', 'KBTU');
        """
        )
        # connection.commit()
        print("[INFO] Data was successfully inserted")        
    
    
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT first_name FROM phone_book WHERE id = 1"""
        )
        print(cursor.fetchone())  
    
    
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE phone_book"""
    #     )
    #     print("[INFO] Table is deleted")  

    cursor = connection.cursor()
    
    update_script = """UPDATE phone_book SET first_name = 'Brother' WHERE phone_number = '87073071821';"""
    cursor.execute(update_script)

    print( ''' Do you want to add new contact?!\n         (0 - No / 1- Yes)''')
    wish = input()
    if wish == '1':
        contact = []
        print(f"Name:")
        name = input()
        contact.append(name)
        print("Phone_number:\n")
        phone_number = input()
        contact.append(phone_number)
        status = input("Status:\n")
        contact.append(status)


        new_contact = ("""INSERT INTO phone_book VALUES 
            (DEFAULT, %s, %s, %s);
        """)
        cursor.execute(new_contact, contact)
        del contact
    else:
        print("Lets continue!")


    cursor.execute("""SELECT first_name FROM phone_book WHERE phone_number = '87073071821';""")
    print(cursor.fetchone())

    deleting_phone('Brother')

    insert_data()

    query_filtering_id()

    query_filtering_range_and_in()

    query_order()

    cursor.close()
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL\n", _ex)
finally:
    if connection is not None: 
        connection.close() 
        print("[INFO] PostgreSQL connection closed")