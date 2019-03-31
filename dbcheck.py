import psycopg2
from config import dbconfig
 
def connectcheck():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = dbconfig()
 
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        print("The database is live.")

        # execute a statement
        cur.execute("SELECT version();")
 
        # display the PostgreSQL database server version
        version = cur.fetchone()
        print("You are connected to - ", version,"\n")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # close the cursor with the PostgreSQL
            cur.close()
            # close the connection with the PostgreSQL
            conn.close()
            print("The database is closed.")
     


connectcheck()