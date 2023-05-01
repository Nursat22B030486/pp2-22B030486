import psycopg2
import random

if __name__ == "__main__":
    connection = None

    try:
        connection = psycopg2.connect(host='localhost', user='postgres', dbname='phone_book', password='i_believe')
        cursor = connection.cursor()
        connection.autocommit = True
    
        # exist = False
        contact = []
        contact.append(input("Please, enter a name: "))
        contact.append(input("Please, enter a phone_number: "))
        contact.append(input("Please, enter a status: "))  
        # cursor.execute("""SELECT * FROM phone_book;""")
        # ###### insert data
        # for row in cursor.fetchall():
        #     if row[1] == contact[0]:
        #         exist = True
        #         answer_1 = input("This contact has already saved!!!\n Would you like to update?!   (Yes | NO)\n")
        #         if answer_1.lower() == "yes":
        #             cursor.execute("CALL update(%s, %s, %s)", contact)
            
        # if exist == False:
        #     contact.append(input("Please, enter a phone_number: "))
        #     contact.append(input("Please, enter a status: ")) 
        #     cursor.execute("""CALL insert(%s, %s, %s)""", contact)

        # ##### delete data
        # answer_2 = input("Would you like to delete exact contact?!   (Yes | NO)\n")
        # if answer_2.lower() == "yes":
        #     name = input("Please, enter a name: ")
        #     cursor.execute("""CALL delete(%s)""", [name,])

        # #### FUNCTIONS
        
        # target = input("In which way would you like to search pattern of the data?! \n      (Name|phone) \n")
        
        
        # if target.lower() == "name":
        #     exact = input("Start || sub || end \n")
        #     pattern = input("Please, enter the pattern which we will find from the table!\n")
        #     if exact.lower() == "start":
        #         cursor.execute(f"""SELECT * FROM search_name ('{pattern}%')""")
        #         for row in cursor.fetchall():
        #             print(row)
        #     elif exact.lower() == "sub":
        #         cursor.execute(f"""SELECT * FROM search_name ('%{pattern}%')""")
        #         for row in cursor.fetchall():
        #             print(row)
        #     elif exact.lower() == "end":
        #         cursor.execute(f"""SELECT * FROM search_name ('%{pattern}')""")
        #         for row in cursor.fetchall():
        #                 print(row)
            
        # elif target.lower() == "phone":
        #     exact = input("Start || sub || end \n")
        #     pattern = input("Please, enter the pattern which we will find from the table!\n")
        #     if exact.lower() == "start":
        #         cursor.execute(f"""SELECT * FROM search_phone ('{pattern}%')""")
        #         for row in cursor.fetchall():
        #             print(row)
        #     elif exact.lower() == "sub":
        #         cursor.execute(f"""SELECT * FROM search_phone ('%{pattern}%')""")
        #         for row in cursor.fetchall():
        #             print(row)
        #     elif exact.lower() == "end":
        #         cursor.execute(f"""SELECT * FROM search_phone ('%{pattern}')""")
        #         for row in cursor.fetchall():
        #             print(row)
            


        ### pagination
        # limit = int(random.randint(0, 5))
        # offset = int(random.randint(1, 3))
        # cursor.execute(f"""SELECT * FROM pagination ({limit}, {offset})""")
        # print(limit, offset)
        # for row in cursor.fetchall():
        #     print(row)
        
        cursor.execute("CALL insert_by_list(%s, %s, %s)", contact)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"You have a problem!!!!!\n {error}")
    finally:
        if connection is not None:
            connection.close()
        print("All queries have done successfully!!!")