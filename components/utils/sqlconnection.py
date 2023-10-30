"""
Module/Script Name: sqlconnection.py

Author(s): M. W. Hefner

Initially Created: 06/28/2023

Last Modified: 10/29/2023

Script Description: this script handles all of the connections to the data server.  Do not put calls to the data server elsewhere in your code - losing track of these can be a hazard.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

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
