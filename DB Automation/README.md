# Database Population Automation Project

## Overview

This project demonstrates the automation of database creation and data population for a car dealership management system using Python scripts. The project utilizes the Faker library for generating realistic test data and the MySQL Connector to interact with the MySQL database.

## Project Structure

The project consists of the following components:

### Main Script

- **Main.py:** This script is the entry point of the automation process. It imports and executes individual scripts for each table creation and data population.

### Individual Scripts

- **Car.py:** Create and populate the Car table.
- **CarCategory.py:** Create and populate the CarCategory table.
- **CarColor.py:** Create and populate the CarColor table.
- **CarEngine.py:** Create and populate the CarEngine table.
- **CarModel.py:** Create and populate the CarModel table.
- **CarVariant.py:** Create and populate the CarVariant table.
- **Customer.py:** Create and populate the Customer table.
- **Finance.py:** Create and populate the Finance table.
- **Installment.py:** Create and populate the Installment table.
- **Payment.py:** Create and populate the Payment table.
- **Sale.py:** Create and populate the Sale table.
- **SalesPerson.py:** Create and populate the SalesPerson table.

## Steps Taken

1. **Database Setup:** The Main.py script starts by checking for an existing database. If found, it drops the database to ensure a clean slate.

2. **Table Creation:** Each individual script corresponds to a specific table. These scripts create the necessary tables, defining primary keys, foreign keys, and attributes for each table.

3. **Data Population:** The same individual scripts handle data population for each table. The Faker library is used to generate random but realistic data for different attributes.

4. **Foreign Key Constraints:** The scripts ensure that foreign key references are maintained, ensuring data integrity across tables.

5. **Automation Benefits:** The automation process eliminates manual errors, ensures consistency in data population, and simplifies the database setup for development and testing.

## Technologies Used

- **Faker Library:** Used to generate realistic data for attributes like names, addresses, dates, etc.

- **MySQL Connector:** Used to interact with the MySQL database, including database creation, table creation, and data insertion.

## How to Run

1. Ensure you have Python installed on your system.

2. Install the required packages using the following command:
    ```shell
    pip install -r requirements.txt
    
3. Modify the database connection parameters in each individual script to match your MySQL server configuration.

4. Run the Main.py script to start the automation process:


## Conclusion

This project showcases the power of automation in database setup and data population for a car dealership management system. By utilizing Python scripts, Faker library, and MySQL Connector, we have successfully streamlined the process, enabling consistent, efficient, and error-free database creation and population.

