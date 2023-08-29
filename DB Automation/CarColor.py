import mysql.connector

# function to create CarColor table
def create_car_color():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cardb")

    cursor = db.cursor()

    car_colors = [
        (1, "White"),
        (2, "Black"),
        (3, "Silver"),
        (4, "Gray"),
        (5, "Red"),
        (6, "Blue"),
        (7, "Green"),
        (8, "Brown"),
        (9, "Yellow"),
        (10, "Orange")
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarColor (
            ColorID INT PRIMARY KEY,
            ColorName VARCHAR(50)
        )
    """)

    insert_query = "INSERT INTO CarColor (ColorID, ColorName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_colors)

    db.commit()
    cursor.close()
    db.close()

    print("CarColor table created and populated successfully.")



