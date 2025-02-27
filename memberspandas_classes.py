

import os
import psycopg2
import configparser
import pandas as pd
class Member:

    member_serial_number = 0

    def __init__(self):
        '''self.id = None
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone_number = None

        self.age = age
        self.address = address
        self.salary = salary
        self.__ssn = None'''

    
    #private method
    def __retrieve_ssn(self):
        print(self.__ssn)

    def retrieve_member_details(self):
        member_serial_number = 20
        #Retrieve details from database using Email
        return "details"
    
    def get_connection(self):
        import configparser
        # Initialize the config parser
        config = configparser.ConfigParser()
        config.read('Users\\sandh\\OneDrive\\Documents\\Python\\Datamodel\\Pandas\\credential.cfg')
        import os
        #from dotenv import load_dotenv
        connection = None
        # Database connection details
        # Default PostgreSQL port
        # Establishing the connection
        try:
            connection = psycopg2.connect(
                dbname=config['postgres']['DB_NAME'],
                user=config['postgres']['DB_USER'],
                password=config['postgres']['DB_PASSWORD'],
                host=config['postgres']['DB_HOST'],
                port=config['postgres']['DB_PORT'],
                sslmode="require"
            )
            print("Database connection successful!")
            
        except Exception as e:
            print("Error connecting to the database:", e)
        return connection

        #save member to database


    def create_new_member(self):

        connection = self.get_connection()
        if(connection is not None):
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO members_test (member_id,first_name, last_name)
            VALUES (%s, %s, %s) RETURNING member_id ;
            """, (self.member_id,self.first_name,self.last_name))
            connection.commit()
            id = cursor.fetchone()[0]
            print(f"Record inserted successfully!: {id}")
        #raise exception if email already exists
        else:
            raise Exception ("connection could not be established")
        return "id of inserted row"
    
    @classmethod
    def retrieve_members(cls):
        from sqlalchemy import create_engine
        import configparser
        import psycopg2
        config = configparser.ConfigParser()
        config.read('C:\\Users\\sandh\\OneDrive\\Documents\\Python\\Datamodel\\Basics\\credential.cfg')

       # Assuming you have a connection to the database
        try:
            # Database connection parameters
            DATABASE_TYPE = 'postgresql'
            DBAPI = 'psycopg2'
            ENDPOINT = config['postgresqlcred']['db_host'] # e.g., localhost or remote server
            USER = config['postgresqlcred']['db_user']
            PASSWORD = config['postgresqlcred']['db_password']
            PORT = 5432 # Default PostgreSQL port
            DATABASE = config['postgresqlcred']['db_name']
            # Creating the engine
            engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
                        
            query = "SELECT * FROM members_test"
            df_postgres = pd.read_sql(query, engine)
            df_postgres.to_csv('members_fromdb.csv', index=False)
            print(df_postgres.head())
            print("Data saved from postgres to csv successfully.")

        except Exception as e:
            print("Error connecting to the database:", e)


Member.retrieve_members()   

#mem = Member()
#mem.first_name = "test"
#mem.last_name = "new"


#new_member = Member(email="classa1@one.com", fname="testclass", lname="testclass")


#new_member.create_new_member()

"""print(new_member.member_serial_number)
print(Member.member_serial_number)

print(new_member.first_name)
print(Member.first_name) #error

print(Member.retrieve_serial_number_class())
print(new_member.retrieve_serial_number_class())

print(Member.retrieve_serial_number_static())
print(new_member.Member.retrieve_serial_number_static())

print(new_member.__ssn)"""