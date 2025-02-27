
import os
from dotenv import load_dotenv
import psycopg2
import configparser
import pandas as pd


from pymongo import MongoClient

class branch:
    #class variable
    number_of_branches = 0
    
    
    def __init__(self, bid, bname=None, bstr=None, bcity=None, bzip=None, bphone=None):
        #instance variable
        self.branch_id = bid
        self.branch_name = bname
        self.stree = bstr
        self.phone = bphone
        self.city = bcity
        self.zip = bzip
        #connect here
        


    def create_branch(self, member_id, name):
        config = configparser.ConfigParser()
        config.read('credentials.cfg')

       # Assuming you have a connection to the database
        try:
            connection = psycopg2.connect(
                dbname=config['postgres']['DB_NAME'],
                user=config['postgres']['DB_USER'],
                password=config['postgres']['DB_PASSWORD'],
                host=config['postgres']['DB_HOST'],
                port=config['postgres']['DB_PORT'],
                sslmode="require"
            )
            cursor = connection.cursor()
            
            #run the insert query

            query = f"insert into branches values (?, ?, ?)".format(self.branch_name, self.address, self.phone)
            cursor.execute(query)

            cursor.commit()
        except Exception as e:
            print("Error connecting to the database:", e)
        finally:    
            if connection:
                cursor.close()
                connection.close()
                #close connection
                #close cursor

    @staticmethod
    def create_branch_from_df():
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
                       
            # Branches DataFrame
            df = pd.read_csv('C:\\Users\\sandh\\OneDrive\\Desktop\\branch.csv')
            # Saving DataFrame to PostgreSQL
            df.to_sql('branch_test1', engine, if_exists='append', index=False)
            print("Data saved to PostgreSQL successfully.")

        except Exception as e:
           # logging.error("Error connecting to the database:", e)
            print("Error connecting to the database:", e)


    @staticmethod
    def create_branch_mongo_from_df():
        import pymongo
        from pymongo.mongo_client import MongoClient

        from pymongo.server_api import ServerApi
        import pandas as pd
        import os
        from dotenv import load_dotenv
        # Load environment variables from .env file
        load_dotenv()

        uri = os.getenv("db_mongo")
        if not uri:
            raise ValueError("Environment variable 'mongo_db' not found. Please set it in the .env file.")
        #print(uri)
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['members_test']
        collection = db['branch']
       # Assuming you have a connection to the database
        try:
                        
            # Branches DataFrame
            df = pd.read_csv('c:\\Users\\sandh\\OneDrive\\Desktop\\branch.csv')

            data_dict = df.to_dict(orient='records')

            # 4. Insert data into MongoDB
            collection.insert_many(data_dict)

            # Close the connection
            client.close()
            print("Data saved to mongodb successfully.")

        except Exception as e:
            print("Error connecting to the database:", e)

    @classmethod
    def retrieve_branch_mongo_from_df(cls):
        import pymongo
        from pymongo.mongo_client import MongoClient
        
        from pymongo.server_api import ServerApi
        import pandas as pd
        import os
        from dotenv import load_dotenv
        # Load environment variables from .env file
        load_dotenv()

        uri = os.getenv("db_mongo")
        #print(uri)
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['members_test']
        collection = db['branch']
       # Assuming you have a connection to the database
        try:
            data = list(collection.find())

            # Branches DataFrame
            df = pd.DataFrame(data)
            
            df['_id'] = df['_id'].astype(str)

            df.to_csv('branches_from_mongo.csv', index=False)
            client.close()
            print("Data read successfully.")

        except Exception as e:
            print("Error connecting to the database:", e)

branch.create_branch_from_df()

#br = branch(2)
#br.create_branch(1, "new branch")

#branch.create_branch(1, "new branch", "new")

#br.create_branch_mongo_from_df()

#branch.create_branch_mongo_from_df()

#branch.retrieve_branch_mongo_from_df()