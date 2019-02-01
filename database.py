import psycopg2

class InitializeDb:

    def __init__(self, url):
        try:
            self.connection = psycopg2.connect(url)
            self.cursor = self.connection.cursor()
            print('A connection to flask_api database was established!')
        except:
            print("A problem occured while connecting to the database")

    def create_tables(self):
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
            id serial PRIMARY KEY NOT NULL,
            title VARCHAR NOT NULL,
            description text NOT NULL,
            timestamp TIMESTAMP NOT NULL
            );
        """)
        self.connection.commit()
