import psycopg2

def connect_to_database():
    try:
        conn = psycopg2.connect(
            database="MyData",
            user="postgres",
            host="localhost",
            password="aruzhan3",
            port=5432
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_phonebook_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook1_list (
                number_id SERIAL PRIMARY KEY,
                full_name VARCHAR(100) NOT NULL,
                phone_number VARCHAR(20) NOT NULL
            );
        """)
        conn.commit()
        print("Table 'phonebook1_list' created successfully")
    except psycopg2.Error as e:
        print("Error creating table:", e)

def insert_data_from_csv(conn, filename):
    try:
        cur = conn.cursor()
        with open(filename, 'r', encoding='UTF-8') as f:
            cur.copy_from(f, 'phonebook1_list', sep=',')
            conn.commit()
        print("Data inserted from CSV file successfully")
    except psycopg2.Error as e:
        print("Error inserting data from CSV file:", e)

# Function to insert data from the console into the database
def insert_data_from_console(conn):
    try:
        cur = conn.cursor()
        number_id = input("Enter id: ")
        full_name = input("Enter full name: ")
        phone_number = input("Enter phone number: ")
        cur.execute(
            "INSERT INTO phonebook1_list (number_id, full_name, phone_number) VALUES (%s, %s, %s)",
            (number_id, full_name, phone_number)
        )
        conn.commit()
        print("Data inserted from console successfully")
    except psycopg2.Error as e:
        print("Error inserting data from console:", e)

# Function to update data in the database
def updating_data(conn):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE phonebook1_list SET phone_number = %s WHERE number_id = %s", ('+7 705 133 1223', '3'))
        conn.commit()
        print("Data updated successfully")
    except psycopg2.Error as e:
        print("Error updating data:", e)

# Function to select data from the database
def select_from_data(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook1_list WHERE number_id ='3';")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("Data selected successfully")
    except psycopg2.Error as e:
        print("Error selecting data:", e)

# Main function to execute the code
def main():
    # Connect to the database
    conn = connect_to_database()
    if conn is None:
        return

    # Create the phonebook1_list table
    create_phonebook_table(conn)

    # Insert data from a CSV file
    insert_data_from_csv(conn, 'pb_data.csv')

    # Insert data from the console
    insert_data_from_console(conn)

    # Update data
    updating_data(conn)

    # Select data
    select_from_data(conn)

    # Close the database connection
    conn.close()
    print("Connection to the database closed")

# Execute the main function
if __name__ == "__main__":
    main()
