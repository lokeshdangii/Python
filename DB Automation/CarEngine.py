import mysql.connector

def create_car_engine():
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cardb"
    )

    cursor = db.cursor()

    car_engines = [
        (1, "Gasoline"),
        (2, "Diesel"),
        (3, "Electric"),
        (4, "Hybrid")
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarEngine (
            EngineID INT PRIMARY KEY,
            EngineName VARCHAR(100)
        )
    """)

    insert_query = "INSERT INTO CarEngine (EngineID, EngineName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_engines)

    db.commit()
    cursor.close()
    db.close()

    print("CarEngine table created and populated successfully.")
