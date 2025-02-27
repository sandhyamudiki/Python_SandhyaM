def create_table(connection,table_name):
    cursor = connection.cursor()
    if(table_name == "members"):
        cursor.execute("""
            create table if not exists members(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                gender VARCHAR(10)
            );
            """)
    elif(table_name == 'accounts'):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id SERIAL PRIMARY KEY,
            balance float not null,
            account_type VARCHAR(20) NOT NULL,
            member_id int,
            created_date date
        );
        """)
    connection.commit()
    print("Table created successfully!")