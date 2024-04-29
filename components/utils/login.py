"""
Provides mechanisms for handling user authentication and authorization within the Dash application,
leveraging Shibboleth for Single Sign-On (SSO) authentication and checking user permissions against an
application-specific metadata stored on a SQL server.

This module includes functions to verify whether a user is authenticated and authorized to access the application,
based on whether the application is marked as public or restricted in the metadata and the user's permissions.

Functions
---------
authenticaedLogin() -> list[bool, str | None]
    Checks if the user is authenticated via Shibboleth SSO by looking for a 'Uid' in the request headers.
    Returns a list where the first element is a boolean indicating authentication status, and the second element
    is the username if authenticated.

userIsAuthorized() -> bool
    Determines if the current user is authorized to access the application. It first checks if the application is public;
    if not, it further checks the user's permissions based on the SQL server's metadata.
    Returns True if the user is authorized, otherwise False.

Examples
--------
>>> login_status = authenticaedLogin()
>>> if login_status[0]:
...     print(f"User {login_status[1]} is authenticated.")
... else:
...     print("User is not authenticated.")

>>> if userIsAuthorized():
...     print("Access granted.")
... else:
...     print("Access denied.")

This module is critical for enforcing security and access control within the application, ensuring that only authorized
users can access specific features or data sets based on the application's operational requirements.

Notes
-----
- The module assumes the presence of a valid Flask request context to access request headers.
- It interfaces with a SQL server managed by 'sqlconnection.py' for reading application and user-specific metadata.

See Also
--------
flask : For handling HTTP request contexts.
components.utils.sqlconnection : For interactions with the SQL server managing application metadata.
"""


import flask
import components.utils.sqlconnection as dataserver

# INTERFACING WITH SHIBBOLETH SINGLE SIGN-ON AUTHENTICATION
#
# THESE ARE USED ONLY IN A REQUESTS CONTEXT.
#
# For sign-on.  Checks if the user is signed into 
# their Appalachian account.  If the application is public, this 
# will show the application regardless.  If restricted, this
# application will only show if the user is authorized on the data
# server in the application metadata.
# Define a callback to check user authentication and authorization

def authenticaedLogin():
    # If Remote-User is available in the header 
    if 'Uid' in flask.request.headers:
        
        # Get the username
        username = flask.request.headers['Uid']

        return [True, username]
    
    else :

        return [False, None]

# Access RIEEE Data Server application metadata to determine if
# the user is authorized for this application.
def userIsAuthorized():

    # First grab application metadata.
    metadata = dataserver.get_application_metadata()
    applicationIsPublic = metadata[0][0][0].lower() == "t"

    # If the application is public, return true.
    if applicationIsPublic:
        return True

    # If there is no request context, ignore and return out
    if not flask.has_request_context():
        return applicationIsPublic

    # Get Log in information
    login = authenticaedLogin()

    if login[1] is not None :

        metadata = dataserver.get_authorization_metadata(login[1])
        userIsAdmin = metadata[0][0][0].lower() == "true"
        userHasPermission = metadata[1][0][0].lower() == "true"

        if userIsAdmin :
            # USER AUTHORIZED
            return True
        if userHasPermission :
            # USER AUTHORIZED
            return True
    
    # otherwise... USER NOT AUTHORIZED
    return False
