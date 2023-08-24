import mysql.connector
from faker import Faker
import random

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cardb"
)

cursor = db.cursor()
fake = Faker()

# Table creation queries
create_table_queries = [
    """
    CREATE TABLE SalesPerson (
        SalesPersonID INT NOT NULL PRIMARY KEY,
        SP_Name VARCHAR(50) NOT NULL,
        Gender VARCHAR(10) NOT NULL,
        DateofBirth DATE NOT NULL,
        MobileNo BIGINT NOT NULL,
        email VARCHAR(100) NOT NULL,
        Adress1 VARCHAR(100) NOT NULL,
        Adress2 VARCHAR(100) NOT NULL,
        City VARCHAR(50) NOT NULL,
        State VARCHAR(50) NOT NULL,
        PinCode VARCHAR(20) NOT NULL
    )
    """,
]

# Execute table creation queries
for query in create_table_queries:
    cursor.execute(query)

# Populate SalesPerson table with sequential IDs within the range (1 to 40)
for sales_person_id in range(1, 40):  # Adjust the range as needed
    insert_query = """
    INSERT INTO SalesPerson (SalesPersonID, SP_Name, Gender, DateofBirth, MobileNo, email, Adress1, Adress2, City, State, PinCode)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        sales_person_id,  # Use sequential SalesPersonID
        fake.name(),
        random.choice(["Male", "Female"]),
        fake.date_of_birth(),
        fake.random_int(min=1000000000, max=9999999999),
        fake.email(),
        fake.street_address(),
        fake.secondary_address(),
        fake.city(),
        fake.state(),
        fake.zipcode()
    )
    cursor.execute(insert_query, data)

# Similarly, you can create and populate other tables

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
