"""
Handles database connections and queries for the Dash application, centralizing the management of data interactions
to ensure consistency and security. This script is responsible for establishing connections to a MySQL server,
executing queries, and managing database interactions such as retrieving application metadata and user permissions.

This module uses a centralized configuration to manage database credentials and settings, ensuring that all database
interactions are performed securely and efficiently.

Functions
---------
connect_to_mysql() -> connection
    Establishes and returns a connection to the MySQL server using predefined configuration settings.

get_research_data() -> list
    Retrieves research data from the MySQL server. This function establishes a connection, executes a SELECT query,
    and returns the fetched data.

get_application_metadata() -> list
    Retrieves metadata for the application from the MySQL server to determine if the application is public or restricted.

get_authorization_metadata(username: str) -> list
    Checks if the specified user has administrative rights or specific permissions for the application based on
    the user's username. Returns a list containing the user's admin status and permission status.

Examples
--------
>>> connection = connect_to_mysql()
>>> if connection.is_connected():
...     print("Successfully connected to the database.")

>>> research_data = get_research_data()
>>> for data in research_data:
...     print(data)

>>> metadata = get_application_metadata()
>>> print("Is application public?", "Yes" if metadata[0][0] == 'true' else "No")

>>> user_permissions = get_authorization_metadata('johndoe')
>>> print("Is user admin?", "Yes" if user_permissions[0][0] == 'true' else "No")
>>> print("Does user have permissions?", "Yes" if user_permissions[1][0] == 'true' else "No")

Notes
-----
- This module relies on a configuration file managed by `config.py` for database connection settings.
- Error handling for database connections and queries is crucial and should be robust to handle any
  interruptions or issues during data retrieval.

Dependencies
------------
mysql.connector : For handling MySQL database connections and executing SQL queries.
components.utils.config : For accessing configuration settings.
components.utils.constants : For accessing application-specific constants like app_id.

See Also
--------
flask : The web framework used for managing the web application context.
"""


from mysql.connector import connect, Error
from components.utils.config import cfg
from components.utils.constants import app_id

# MySQL connection configuration
config = {
    'user': cfg.get('app', 'dbuser'),
    'password': cfg.get('app', 'dbpass'),
    'host': cfg.get('app', 'dbhost'),
    'port': cfg.get('app', 'dbport'),
    'database': cfg.get('app', 'dbname'),
    'ssl_ca': './assets/rieeedata.crt'
}

# Metadata connection configuration
metadata_config = {
    'user': cfg.get('app', 'dbuser'),
    'password': cfg.get('app', 'dbpass'),
    'host': cfg.get('app', 'dbhost'),
    'port': cfg.get('app', 'dbport'),
    # All applications have permission to look at datadash metadata...
    # kind of weird. May want to find a different way of interfacing
    # application metadata eventually.
    'database': 'datadash_application',
    'ssl_ca': './assets/rieeedata.crt'
}

# Function to establish a MySQL connection
def connect_to_mysql():
    try:
        connection = connect(**config)
        # This can be helpful for debugging
        # print("Connected to MySQL server...")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL server: {e}. Are you connected to App's VPN?")
        exit(1)

# Function to retrieve data from data server
# 
# It is possible to create callbacks in this file for live-update data
def get_research_data():

    connection = connect_to_mysql()
    cursor = connection.cursor()

    sql = '''
    SELECT * FROM static
    '''
    
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_application_metadata():
    # Grabs the metadata for the application

    # Establish a secure connection to the MySQL server for application data
    try:
        metadata_connection = connect(**metadata_config)
        # this can be helpful for debugging
        #print("Connected to MySQL server...")
    except Error as e:
        print(f"Error connecting to MySQL server: {e}.  Are you connected to App's VPN?")
        exit(1)

    # Create a cursor object to execute SQL queries
    metadata_cursor = metadata_connection.cursor()

    # Is the application public?---------------------------------
    applicationIsPublic = '''
    SELECT CASE
        WHEN EXISTS (SELECT 1 FROM Applications WHERE app_id = ''' + str(app_id) + ''' AND permission_level = 'Public') THEN 'true'
        ELSE 'false'
    END AS result;
    '''
    metadata_cursor.execute(applicationIsPublic)
    applicationIsPublic = metadata_cursor.fetchall()

    return applicationIsPublic


def get_authorization_metadata(username):
    # this retrieves metadata from the RIEEE data server about this 
    # application and whether or not the user has authorization
    # to access the application.  I highly recommend not fooling
    # around here.

    # Establish a secure connection to the MySQL server for application data
    try:
        metadata_connection = connect(**metadata_config)
        # this can be helpful for debugging
        #print("Connected to MySQL server...")
    except Error as e:
        print(f"Error connecting to MySQL server: {e}.  Are you connected to App's VPN?")
        exit(1)

    # Create a cursor object to execute SQL queries
    metadata_cursor = metadata_connection.cursor()



    # Is the user an admin?---------------------------------
    userIsAdmin = '''
    SELECT CASE
        WHEN EXISTS (SELECT 1 FROM Users WHERE username = ''' + "'" + username + "'" + ''' AND user_type = 'ADMIN') THEN 'true'
        ELSE 'false'
    END AS result;
    '''
    metadata_cursor.execute(userIsAdmin)
    userIsAdmin = metadata_cursor.fetchall()

    # Does the user have explicit permission?----------------------
    userHasPermission = '''
    SELECT CASE
        WHEN EXISTS (SELECT 1 FROM User_Application_Permissions WHERE username = ''' + "'" + username + "'" + ''' AND app_id = ''' + str(app_id) + ''') THEN 'true'
        ELSE 'false'
    END AS result;
    '''
    metadata_cursor.execute(userHasPermission)
    userHasPermission = metadata_cursor.fetchall()

    return [userIsAdmin, userHasPermission]
