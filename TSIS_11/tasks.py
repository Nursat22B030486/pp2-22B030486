import psycopg2

"""
RegEx пен адмның аттары арқылы жүгіріп шығып, үзіндіні тапса, консольдан шығару; 
"""
# def function_with_pattern(pattern):
#     query = f"""SELECT * FROM phone_book WHERE first_name ~~ '{pattern}%';""" # ~~* => ILIKE and !~~* vise versa || ^@  => starts_with()

#     cursor.execute(query)
#     for row in cursor.fetchall():
#         print(row)

# def function_with_RegEx_name(pattern):
#     query = f"""SELECT * FROM phone_book WHERE first_name ~ '^.*{pattern}.*$';"""
#     cursor.execute(query)
#     for row in cursor.fetchall():
#         print(row)


# def function_with_RegEx_phone(pattern):
#     query = f"""SELECT * FROM phone_book WHERE phone_number ~ """
#     cursor.execute(query)
#     for row in cursor.fetchall():
#         print(row)




if __name__ == "__main__":
    connection = None

    try:
        connection = psycopg2.connect(host='localhost', user='postgres', dbname='phone_book', password='i_believe')
        cursor = connection.cursor()
        connection.autocommit = True
        
        
        # function_with_pattern(pattern)
        # target = input("In which way would you like to search pattern of the data?! \n      (Name|phone) \n")
        # pattern = input("Please, enter the pattern which we will find from the table!\n")
        
        # if target.lower() == "name":
        #     function_with_RegEx_name(pattern)
        # elif target.lower() == "phone":
        #     function_with_RegEx_phone(pattern)
        contact = []
        contact.append(input("Please, enter a name: "))
        contact.append(input("Please, enter a phone_number: "))
        contact.append(input("Please, enter a status: "))
        print(contact)
        
        cursor.execute("CALL update(%s, %s, %s)", contact)

        cursor.execute("""SELECT * FROM phone_book""")
        for row in cursor.fetchall():
            print(row)

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"You have a problem!!!!!\n {error}")
    finally:
        if connection is not None:
            connection.close()
        print("All queries have done successfully!!!")




