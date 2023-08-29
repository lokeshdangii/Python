# import all the modules/files
from CarColor import create_car_color
from CarCategory import create_car_category
from CarEngine import create_car_engine
from CarModel import create_car_model
from CarVariant import create_car_variant
from Car import create_car
from Customer import create_customer
from SalesPerson import create_salesperson
from Installment import create_installment
from Payment import create_payment
from Sale import create_sale
from Finance import create_finance
import mysql.connector


#function
def create_database():
    
    # Connect to MySQL server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor = db.cursor()

    # Drop the database if it exists
    cursor.execute("DROP DATABASE IF EXISTS cardb")

    # Create a new database
    new_db = "cardb"
    create_database_query = f"CREATE DATABASE {new_db}"
    cursor.execute(create_database_query)

    print(f"\nDatabase '{new_db}' created successfully.\n")

    # Close the connection
    cursor.close()
    db.close()

    create_car_color()
    create_car_category()
    create_car_engine()
    create_car_model()
    create_car_variant()
    create_car()
    create_customer()
    create_salesperson()
    create_installment()
    create_payment()
    create_sale()
    create_finance()


# Driver Code
# main function
if __name__ == "__main__":
    create_database()
