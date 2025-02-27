def greet(name):
    return f"Hello, {name}!"



def create_member(connection, first_name, last_name, gender:None):
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO members (fname, lname, gender)
    VALUES (%s, %s, %s);
    """, (first_name,last_name, gender))
    connection.commit()
    #id = cursor.fetchone()[0]
    print(f"Record inserted successfully!")


def retrieve_members(connection, member_id=None):
    cursor = connection.cursor()
    if(member_id is None):
        query = "SELECT * FROM members;"
    else:
        query = f"SELECT * FROM members where id = {member_id};"
        #query = "SELECT * FROM members where id = " + member_id
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(row)


def update_member(connection, member_id, first_name, last_name):
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE members
    SET first_name = %s, last_name = %s
        WHERE id = %s;
    """, (first_name, last_name, member_id))
    #connection.commit()
    print("Record updated successfully!")
    print("updated data")
    retrieve_members(connection, member_id)


def delete_member(connection, member_id):
    cursor = connection.cursor()
    cursor.execute(f"""
    DELETE FROM members
    WHERE id = {member_id};
    """)
    connection.commit()
    print("Record deleted successfully!")