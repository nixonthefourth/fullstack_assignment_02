# db_raw.py
# Imports
import MySQLdb

# Get Connection
def get_connection():
    # Define Connection Parameters
    conn = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "0777",
        db = "notice_base",
        charset="utf8mb4"
    )

    return conn

"""GET"""

# Get Driver's Details by ID
def fetch_driver_details(driver_id: int):
    # Open SQL Conection
    conn = get_connection()
    cursor = conn.cursor()

    # SQL Query
    query = """SELECT *
    FROM driver_details
    WHERE driver_id = %s;
    """

    # Execute Query
    cursor.execute(query, (driver_id,))
    row = cursor.fetchone()

    # Close Connection
    cursor.close()
    conn.close()

    # Output Results
    return row

# Get Notices Based on the Driver's ID
def fetch_driver_notices(driver_id: int):
    # Open SQL Bridge
    conn = get_connection()
    cursor = conn.cursor()

    # SQL Query
    """
        Extracts the notice details based solely
        on the driver's ID. The normalisation indirectly
        links the driver's ID and notice ID field through
        the car's ID, since the notices are directly
        written on cars and inherited to the owner.
    """

    query = """
    SELECT *
    FROM notice_info
    JOIN car_details ON notice_info.car_id = car_details.car_id
    WHERE car_details.driver_id = %s
    """

    # Execute Query
    cursor.execute(query, (driver_id,))
    row = cursor.fetchone()

    # Close Connection
    cursor.close()
    conn.close()

    # Output Results
    return row

# Get All Driver's
def fetch_all_drivers():
    # Open an SQL Bridge
    conn = get_connection()
    cursor = conn.cursor()

    # Query
    query = """
    SELECT driver_id, state_issue, last_name, first_name
    FROM driver_details
    """

    # Execute Query
    cursor.execute(query)
    row = cursor.fetchall()

    # Close Connection
    cursor.close()
    conn.close()

    # Output Results
    return row

"""POST"""

# Create a New Driver
def create_driver(driver, address):
    # Open SQL Connection
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Check ZIP
        cursor.execute(
            "SELECT 1 FROM reg_zip_code WHERE zip_code = %s",
            (address.zip_code,)
        )

        # If the ZIP doesn't exist, we can insert it
        if cursor.fetchone() is None:
            cursor.execute(
                """
                INSERT INTO reg_zip_code (zip_code, state, city)
                VALUES (%s, %s, %s)
                """,
                (address.zip_code, address.state, address.city)
            )

        # Insert Address
        cursor.execute(
            """
            INSERT INTO reg_address (zip_code, street, house)
            VALUES (%s, %s, %s)
            """,
            (address.zip_code, address.street, address.house)
        )

        address_id = cursor.lastrowid

        # Insert Driver
        cursor.execute(
            """
            INSERT INTO driver_details (
                address_id,
                licence_number,
                state_issue,
                last_name,
                first_name,
                dob,
                height_inches,
                weight_pounds,
                eyes_colour
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                address_id,
                driver.licence_number,
                driver.state_issue,
                driver.last_name,
                driver.first_name,
                driver.dob,
                driver.height_inches,
                driver.weight_pounds,
                driver.eyes_colour
            )
        )

        driver_id = cursor.lastrowid
        conn.commit()
        return driver_id

    # In case things go south – roll back
    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()
