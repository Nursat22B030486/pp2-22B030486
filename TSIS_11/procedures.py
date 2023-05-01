import psycopg2

postgreSQL = {
    'host' : 'localhost',
    'user' : 'postgres',
    'dbname' : 'phone_book',
    'password' :'i_believe'
}

connection = None
try:
    connection = psycopg2.connect(**postgreSQL)
    connection.autocommit = True
    cursor = connection.cursor()
    procedures = []

    procedure_update = """
    CREATE OR REPLACE PROCEDURE update(new_name VARCHAR, new_number VARCHAR, new_status VARCHAR)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        UPDATE phone_book SET 
            phone_number = new_number,
            status = new_status
            WHERE first_name = new_name;
    END;
    $$
    """
    # procedures.append(procedure_update)
    procedure_insert = """
        CREATE OR REPLACE PROCEDURE insert(new_name VARCHAR, new_number VARCHAR, new_status VARCHAR)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            INSERT INTO phone_book VALUES (DEFAULT, new_name, new_number, new_status); 
        END;
        $$
    """
    # procedures.append(procedure_insert)
    procedure_delete = """
        CREATE OR REPLACE PROCEDURE delete(new_name VARCHAR)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            DELETE FROM phone_book WHERE first_name = new_name;
        END;
        $$
    """
    create_type = """
        CREATE TYPE info AS(
            new_name  varchar(55),
            phone_number  varchar(13),
            status  varchar(15)
        );
    """
    cursor.execute(create_type)
    # procedures.append(procedure_delete)
    procedure_add = """
        CREATE OR REPLACE PROCEDURE insert_by_list(info_array info[])
        LANGUAGE plpgsql
        AS $$
        DECLARE 
            info_element info;
            return_info info;
        BEGIN
            FOREACH  info_element IN ARRAY info_array
            LOOP
                IF info_element.phone_number ~~ '8%' then 
                    INSERT INTO phone_book VALUES (DEFAULT, info_element.new_name, info_element.phone_number, info_element.status);
                ELSE 
                    RAISE EXCEPTION '%', info_element.phone_number;
                END IF;
            END LOOP;
        END;
        $$
    """
    # procedures.append(procedure_add)

    # for procedure in procedures:
    #     cursor.execute(procedure)
    cursor.execute(procedure_add)
    cursor.execute(procedure_delete)
    cursor.execute(procedure_insert)
    cursor.execute(procedure_update)
   
    cursor.close()
except (Exception, psycopg2.DatabaseError)  as error:
    print('You have a problem !!! \n', error)
finally:
    if connection is not None:
        connection.close()
        print("All queries have done successfully!!!")
    
    
    # procedure_1 = """
    #         CREATE OR REPLACE PROCEDURE insert_contact(first_name VARCHAR, new_number VARCHAR, new_status VARCHAR, lenght INT)
    #         LANGUAGE plpgsql
    #         AS $$
    #         BEGIN
    #         DECLARE 
    #             count INT
    #             FOR row IN 
    #                 SELECT first_name FROM phone_number 
    #             LOOP
    #                 IF row == first_name THEN
    #                 UPDATE phone_book SET 
    #                     phone_number = new_number,
    #                     status = new_status
    #                 ELSE 
    #                     INSERT INTO phone_book VALUES (DEFAULT, user_name, phone_number, status);
    #                 END IF; 
    #                 count:= count + 1;
    #                 EXIT WHEN count >= lenght;
    #             END LOOP;
    #         END;
    #         $$
    #     """